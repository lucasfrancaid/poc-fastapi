from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_main_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World, it is FastAPI!'}

