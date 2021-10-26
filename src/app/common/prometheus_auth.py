import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException
from app.services.secret_service import load_prometheus_secrets

security = HTTPBasic()


def authorize(credentials: HTTPBasicCredentials = Depends(security)):

    (prometheus_username, prometheus_password) = load_prometheus_secrets()

    is_user_ok = secrets.compare_digest(credentials.username,
                                        prometheus_username)
    is_pass_ok = secrets.compare_digest(credentials.password,
                                        prometheus_password)

    if not (is_user_ok and is_pass_ok):
        raise HTTPException(
            status_code=401,
            detail=f"Access unauthorized, wrong username and password")