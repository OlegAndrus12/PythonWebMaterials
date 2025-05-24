from sqlalchemy import and_
from .db import session
from .models import User, Todo


def get_user(login):
    user = session.query(User).filter(User.login == login).one()
    return user


def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()


def get_all_todos(user):
    todos = session.query(Todo).join(User).filter(Todo.user == user).all()
    return todos


def update_todo(_id, title, description, user):
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
    todo.update({'title': title, 'description': description})
    session.commit()
    return todo.one()


def remove_todo(_id, user):
    r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).delete()
    session.commit()
    return r

def close_connection():
    session.close()
    
