from fastapi import APIRouter
from src.entities.user import User


router = APIRouter()


fake_users_db = [
    User(id=1, name='Lucas', email='lucas@gmail.com'),
    User(id=2, name='Fulano', email='Fulano@gmail.com'),
    User(id=3, name='Ciclano', email='Ciclano@gmail.com'),
    User(id=4, name='Beltrano', email='Beltrano@gmail.com'),
    User(id=5, name='Feltrano', email='Feltrano@gmail.com'),
]


@router.post('')
def create(user: User):
    user.id = fake_users_db[-1].id + 1
    fake_users_db.append(user)
    return {'message': 'User was created!'}

@router.get('/')
async def list_pagination(skip: int = 0, limit: int = 10):
    return {'users': fake_users_db[skip: skip + limit]}

@router.get('/{user_id}')
def read(user_id: int):
    return {'user': [user for user in fake_users_db if user.id == user_id]}

@router.patch('/{user_id}')
def update(user_id: int, user: User):
    index = [index for index, user in enumerate(fake_users_db) if user.id == user_id]
    user.id = fake_users_db[index[0]].id
    fake_users_db[index[0]] = user
    return {'message': 'User was updated!'}

@router.delete('/{user_id}')
def delete(user_id: int):
    user = [user for user in fake_users_db if user.id == user_id]
    fake_users_db.remove(user[0])
    return {'message': 'User was deleted!'}

