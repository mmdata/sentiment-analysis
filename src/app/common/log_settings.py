from inspect import getframeinfo, stack
import structlog
logger = structlog.get_logger()


def initialise_logger(method: str, path: str,
                      trace_id: str) -> structlog.stdlib.BoundLogger:
    log = logger.bind(request_trace_id=trace_id,
                      request_method=method,
                      request_uri=path)
    return log