from fastapi import APIRouter, Depends

from app.config import get_settings, Settings
<<<<<<< HEAD
import os 

=======
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369

router = APIRouter()


@router.get("/status")
async def status(settings: Settings = Depends(get_settings)):
<<<<<<< HEAD
    example_env_variable = os.environ['ENV_VARIABLE_EXAMPLE']
    return {
        "status": "ok!",
        "environment": settings.environment,
        "example_env_variable": example_env_variable,
=======
    return {
        "status": "ok!",
        "environment": settings.environment,
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
        "testing": settings.testing
    }