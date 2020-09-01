from fastapi import APIRouter
from src.entities.auth import Auth


router = APIRouter()


@router.post('/login')
def auth(auth: Auth):
    return {'username': auth.username, 'password': auth.password}

