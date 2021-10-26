import json
#from app.main import create_application
#from fastapi.testclient import TestClient
import os

#app_root_path = os.path.abspath(__file__).replace('src/tests/test_bert.py', '')


def test_not_authenticated(test_app):
    #payload = {'text': "This is a super good movie"}
    response = test_app.get("/svm/httpbasicauth")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()['detail']