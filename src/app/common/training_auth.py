import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException
from app.services.secret_service import load_training_secrets

security = HTTPBasic()


def authorize(credentials: HTTPBasicCredentials = Depends(security)):

    (training_username, training_password) = load_training_secrets()

    is_user_ok = secrets.compare_digest(credentials.username,
                                        training_username)
    is_pass_ok = secrets.compare_digest(credentials.password,
                                        training_password)

    if not (is_user_ok and is_pass_ok):
        raise HTTPException(
            status_code=401,
            detail=f"Access unauthorized, wrong username and password")