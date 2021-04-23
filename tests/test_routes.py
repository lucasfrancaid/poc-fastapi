from fastapi import Body
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_route_auth_login():
    login = {'username': 'lucas', 'password': '123'}
    response = client.post('/auth/login', json=login)
    assert response.status_code == 200

def test_route_users():
    response = client.get('/users/')
    assert response.status_code == 200

