import datetime
from functools import partial
import logging.config
from pythonjsonlogger import jsonlogger
from .__build_info import build_info
import uuid
import random
import os
import re
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(),
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


def rename_fields(key_list, message_dict, log_record):
    if "timestamp" in key_list:
        now = datetime.datetime.now().isoformat()
        log_record["logger_time"] = str(now)
        # remove timestamp key from dictionary
        del message_dict["timestamp"]
    if "level" in key_list:
        log_record["logger_level"] = message_dict["level"].upper()
        del message_dict["level"]

    return message_dict, log_record


def add_build_info(log_record, build_info):
    if "application_version" not in log_record:
        log_record["application_version"] = build_info['version']
    #if "application_instance" not in log_record:
    #    log_record["application_instance"] = os.environ['HOSTNAME']
    if "application_name" not in log_record:
        log_record["application_name"] = build_info['serviceName']
    return log_record


def add_required_missing_keys(log_record):
    """
    Gunicorn logs do not have all the required keys,
    therefore we set some of them here. 
    """

    keys = [
        "logger_name", "logger_line", "request_trace_id", "logger_level",
        "context_account_name", "context_account_id", "context_company_name",
        "context_company_id", "context_user_id"
    ]
    for key in keys:
        if key not in log_record:
            log_record[key] = 'NOT_SET'

    if "logger_time" not in log_record:
        now = datetime.datetime.now().isoformat()
        log_record["logger_time"] = str(now)
    if "request_method" not in log_record:
        for method in ['GET', 'POST', 'PUT']:
            if method in log_record['logger_message']:
                log_record["request_method"] = method
                break
            else:
                log_record["request_method"] = 'NOT_SET'
    if "request_uri" not in log_record:
        for method in ['GET', 'POST', 'PUT']:
            uri = re.search(f'{method} (.*) HTTP',
                            log_record['logger_message'])
            if uri:
                log_record["request_uri"] = uri.group(1)
                break
            else:
                log_record["request_uri"] = 'NOT_SET'

    return log_record


class JsonLogFormatter(jsonlogger.JsonFormatter):  # pragma: no cover
    def add_fields(self, log_record, record, message_dict):
        """
        This method allows us to inject custom data into resulting log messages
        and it's used to forma in the same way logs from FastAPI and Gunicorn.
        message_dict: contains the logs as initially formatted by gunicorn or FastAPI
        log_record: is the actual final log dictionary
        """

        # get the required field
        for field in self._required_fields:
            if field == "message":
                log_record["logger_message"] = record.__dict__.get(field)

        for key, value in record.__dict__.items():
            # this allows to have numeric keys
            if key == "lineno":
                log_record["logger_line"] = value
            if key == "pathname":
                log_record["logger_name"] = value

        # get keys initially in the logs
        key_list = list(message_dict.keys())

        # update with the informations coming from FastAPI
        log_record.update(message_dict)

        message_dict, log_record = rename_fields(key_list, message_dict,
                                                 log_record)

        log_record = add_build_info(log_record, build_info)
        log_record = add_required_missing_keys(log_record)
        log_record.update(message_dict)

        # This will delete the keys that are considered RESERVED_ATTRS
        # in https://github.com/madzak/python-json-logger/blob/master/src/pythonjsonlogger/jsonlogger.py.
        # Thus we have to save the lineno before.
        jsonlogger.merge_record_extra(record,
                                      log_record,
                                      reserved=self._skip_fields)
