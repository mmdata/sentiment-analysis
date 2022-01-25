<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict
=======
from fastapi import APIRouter, HTTPException, Depends, Request, Header
from typing import Dict, Optional
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
from app.models.pydantic_models import TrainPayloadSchema
from app.models.pydantic_models import PredictPayloadSchema
from app.services.linear_svm.predict_svm import predict_svm
from app.services.linear_svm.train_svm import train_svm
from app.services.linear_svm.metrics_svm import metrics_svm
from app.common.training_auth import authorize
from concurrent.futures import ThreadPoolExecutor
<<<<<<< HEAD
=======
from app.config import log
from app.common.log_settings import initialise_logger
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369

router = APIRouter()
executor = ThreadPoolExecutor(2)


@router.get("/svm/httpbasicauth")
async def example_basic_auth(username: str = Depends(authorize)):
    """
    Example of http basic auth protected route
    """
    return {"username": username}


@router.post("/svm/train")
<<<<<<< HEAD
async def train(payload: TrainPayloadSchema) -> Dict:

    password = payload.password
    ### OPEN NEW THREAD
    executor.submit(train_svm)
=======
async def train(
    payload: TrainPayloadSchema,
    request: Request,
    x_request_id: Optional[str] = Header(None)) -> Dict:

    if x_request_id == None:
        x_request_id = 100

    log = initialise_logger(
        method=request.method,
        path=request.url.path,
        trace_id=x_request_id,
    )
    log.info(logger_message="train endpoint was called")
    password = payload.password
    ### OPEN NEW THREAD
    executor.submit(train_svm, log)
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369

    response_object = {"message": "we are training the model"}
    return response_object


@router.post("/svm/predict")
async def predict(payload: PredictPayloadSchema) -> Dict:

    text_tobe_analysed = payload.text
    prediction = "we could not asses the sentiment"
    prediction = predict_svm(text_tobe_analysed)

    response_object = {"message": f"your review is: {prediction[0]}"}
    return response_object


@router.get("/svm/metrics")
async def metrics() -> Dict:

    response_object = metrics_svm()
    response_object["model"] = "svm"

    return response_object