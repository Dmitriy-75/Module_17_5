# В модуле user.py создайте модель User, наследованную от ранее написанного Base со следующими атрибутами:
# __tablename__ = 'users'
# id - целое число, первичный ключ, с индексом.
# username - строка.
# firstname - строка.
# lastname - строка.
# age - целое число.
# slug - строка, уникальная, с индексом.
# tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.

from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))