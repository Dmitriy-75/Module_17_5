# Напишите логику работы функций маршрутов аналогично предыдущему заданию:


# Функция update_task ('/update') - идентично update_user.
# Функция delete_task ('/delete') - идентично delete_user.

# Подготовьтесь и импортируйте все необходимые классы и функции (ваши пути могут отличаться):
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db

from typing import Annotated
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask

from sqlalchemy import insert, select, update, delete
from slugify import slugify
from fastapi import FastAPI, APIRouter

router=APIRouter(prefix="/task",tags=["task"])
DbSession = Annotated[Session, Depends(get_db)]

# В модуле task.py:
# Функция all_tasks ('/') - идентично all_users.
# Функция task_by_id ('/task_id') - идентично user_by_id (тоже по id)

@router.get("/")
async def all_tasks(db: DbSession):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(task_id:int, db: DbSession):
    by_id_task = db.scalars(select(Task).where(Task.id == task_id))
    if by_id_task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")
    return by_id_task


# Функция craete_task ('/create'):
# Дополнительно принимает модель CreateTask и user_id.
# Подставляет в таблицу Task запись значениями указанными в CreateUser и user_id, если пользователь найден.
# Т.е. при создании записи Task вам необходимо связать её с конкретным пользователем User.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# В случае отсутствия пользователя выбрасывает исключение с кодом 404 и описанием "User was not found"

@router.post("/create")
async def create_task(db: DbSession, cr_task: CreateTask, user_id: int):

    check_id = db.scalars(select(User).where(User.id == user_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")

    db.execute(insert(Task).values(title=cr_task.title,
                                   content=cr_task.content,
                                   priority=cr_task.priority,
                                   slug=slugify(cr_task.title),
                                   user_id=user_id
                                   ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_task(db: DbSession, task_id:int, upd_user: UpdateTask):
    check_id = db.scalars(select(Task).where(Task.id == task_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")

    db.execute(update(Task).where(Task.id == task_id).values(
                                title=upd_user.title,
                                contetnt=upd_user.contetnt,
                                priority=upd_user.priority))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.delete("/delete")
async def delete_task(db: DbSession, task_id:int):
    check_id = db.scalars(select(Task).where(Task.id == task_id))
    if check_id is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}