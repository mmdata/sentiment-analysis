import json
#from app.main import create_application
#from fastapi.testclient import TestClient
import os


def test_status(test_app):
    response = test_app.get("/status")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "status": "ok!",
        "testing": True
    }


#from app.main import create_application
#from fastapi.testclient import TestClient
#import os

#test_app = create_application()
#client = TestClient(test_app)

#app_root_path = os.path.abspath(__file__).replace('src/tests/test_status.py',
#                                                  '')

#def test_status():
#    response = client.get("/status")
#    assert response.status_code == 200
#    assert response.json() == {
#        "environment": "dev",
#        "status": "ok!",
#        "testing": True
#    }

#from app import main

#def test_status(test_app):
#    response = test_app.get("/status")
#    assert response.status_code == 200
#    assert response.json() == {
#        "environment": "dev",
#        "ping": "pong!",
#        "testing": True
#    }
