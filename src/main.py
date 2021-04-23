from fastapi import FastAPI, Body
from src.controllers import auth, users


app = FastAPI()

app.include_router(auth.router, tags=['Auth'], prefix='/auth')
app.include_router(users.router, tags=['Users'], prefix='/users')

@app.get('/')
async def root():
    return {'message': 'Hello World, it is FastAPI!'}

