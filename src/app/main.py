import os

from fastapi import FastAPI, Depends

from app.api import status
from app.api import linear_svm
from app.common.prometheus_auth import authorize
from prometheus_fastapi_instrumentator import Instrumentator


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(status.router)
    application.include_router(linear_svm.router)

    #Instrumentator().instrument(application).expose(
    #    app=application,
    #    endpoint='/prometheus/metrics',
    #    dependencies=[Depends(authorize)])

    return application
