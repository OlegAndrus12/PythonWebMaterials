
from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.orm import mapped_column, Mapped, sessionmaker, declarative_base

engine = create_engine("sqlite:///./users.db")
Session = sessionmaker(engine)
session = Session(bind=engine)
Base = declarative_base()
# class User:
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String)
     

class User(Base):
    __tablename__ = "users"
    id: int = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)

Base.metadata.create_all(engine)