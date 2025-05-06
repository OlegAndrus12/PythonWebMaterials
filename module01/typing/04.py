#pip install pydantic

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=30)     # OK
user = User(name="Bob", age="thirty") # Raises ValidationError
