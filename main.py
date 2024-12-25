# В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция возвращает словарь
# - {"message": "Welcome to Taskmanager"}.
# Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все маршруты в одно приложение.
from fastapi import FastAPI, APIRouter
from app.routers import task
from app.routers import user

app = FastAPI()
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

# python -m uvicorn main:app