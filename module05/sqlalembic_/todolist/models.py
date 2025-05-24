from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Admin(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25), nullable=False, unique=True)
    password = Column(String(25), nullable=False)


