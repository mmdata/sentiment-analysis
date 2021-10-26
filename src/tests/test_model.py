import json
#from app.main import create_application
#from fastapi.testclient import TestClient
import os

#app_root_path = os.path.abspath(__file__).replace('src/tests/test_bert.py', '')


def test_model_positive(test_app):
    payload = {'text': "This is a super good movie"}
    response = test_app.post("/svm/predict", data=json.dumps(payload))
    assert response.status_code == 200
    assert 'positive' in response.json()['message']


def test_model_negative(test_app):
    payload = {'text': "This is a very bad movie"}
    response = test_app.post("/svm/predict", data=json.dumps(payload))
    assert response.status_code == 200
    assert 'negative' in response.json()['message']
