from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class User(BaseModel):
    id: Optional[int] = 0
    name: str
    email: str
    phone: Optional[str] = None 


fake_users_db = [
    User(id=1, name='Lucas', email='lucas@gmail.com'),
    User(id=2, name='Fulano', email='Fulano@gmail.com'),
    User(id=3, name='Ciclano', email='Ciclano@gmail.com'),
    User(id=4, name='Beltrano', email='Beltrano@gmail.com'),
    User(id=5, name='Feltrano', email='Feltrano@gmail.com'),
]


"""
Path root
"""
@app.get('/')
async def root():
    return {'message': 'Hello World, it is FastAPI!'}

"""
Path with fixed parameter
"""
@app.get('/users/me')
def read_me():
    return {'user': 'I am you!'}

"""
Path to get user with int parameter
"""
@app.get('/users/{user_id}')
def read(user_id: int):
    return {'user': [user for user in fake_users_db if user.id == user_id]}

"""
Path to get users with pagination using query parameters
"""
@app.get('/users/')
async def read_pagination(skip: int = 0, limit: int = 10):
    return {'users': fake_users_db[skip: skip + limit]}

"""
Path to create user with User model
"""
@app.post('/users')
def create_user(user: User):
    user.id = fake_users_db[-1].id + 1
    fake_users_db.append(user)
    return {'message': 'User was created!'}

"""
Path to create anything with Body accepting anything data
"""
@app.post('/any')
def create_any(body = Body(...)):
    return {'body': body}

"""
Path to update user by id using path parameter
"""
@app.patch('/users/{user_id}')
def update(user_id: int, user: User):
    index = [index for index, user in enumerate(fake_users_db) if user.id == user_id]
    user.id = fake_users_db[index[0]].id
    fake_users_db[index[0]] = user
    return {'message': 'User was updated!'}

"""
Path to delete an user by id with path parameter
"""
@app.delete('/users/{user_id}')
def delete(user_id: int):
    user = [user for user in fake_users_db if user.id == user_id]
    fake_users_db.remove(user[0])
    return {'message': 'User was deleted!'}

