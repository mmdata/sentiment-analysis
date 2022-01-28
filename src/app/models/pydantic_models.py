from pydantic import BaseModel, validator
from typing import Optional


class TrainPayloadSchema(BaseModel):
    password: str

class TrainParametersSchema(BaseModel):
    random_state: Optional[int] = None
    max_iter: Optional[int] = 1000
    penalty: str
    @validator('penalty')
    def jboard_must_be_in_list(cls, penalty):
      allowed_penalties=["l1", "l2"]
      if penalty not in allowed_penalties:
        raise ValueError(f'jboard must be in {allowed_penalties}')
      return penalty

    class Config:
        schema_extra = {
            "example": {
                "random_state": 1,
                "max_iter": 1000,
                "penalty": "l1"
            }
        }


class PredictPayloadSchema(BaseModel):
    text: str
    class Config:
        schema_extra = {
            "example": {
                "text": "The movie was extremely good"
            }
        }