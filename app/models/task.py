
# Модели баз данных:
# В модуле task.py создайте модель Task, наследованную от ранее написанного Base со следующими атрибутами:
# __tablename__ = 'tasks'
# id - целое число, первичный ключ, с индексом.
# title - строка.
# content - строка.
# priority - целое число, по умолчанию 0.
# completed - булевое значение, по умолчанию False.
# user_id - целое число, внешний ключ на id из таблицы 'users', не NULL, с индексом.
# slug - строка, уникальная, с индексом.
# user - объект связи с таблицей с таблицей User, где back_populates='tasks'.

from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))