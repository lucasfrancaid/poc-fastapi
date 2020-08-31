from fastapi import APIRouter


router = APIRouter()


@router.post('/login')
def auth(username: str, password: str):
    return {'username': username, 'password': password}

