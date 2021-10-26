from pydantic import BaseModel


class TrainPayloadSchema(BaseModel):
    password: str


class PredictPayloadSchema(BaseModel):
    text: str