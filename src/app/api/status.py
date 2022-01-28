from fastapi import APIRouter, Depends

from app.config import get_settings, Settings
import os 


router = APIRouter()


@router.get("/status")
async def status(settings: Settings = Depends(get_settings)):
    example_env_variable = os.environ['ENV_VARIABLE_EXAMPLE']
    return {
        "status": "ok!",
        "environment": settings.environment,
        "example_env_variable": example_env_variable,
    }