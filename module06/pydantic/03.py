
from pydantic import BaseModel, field_validator, EmailStr

class Person(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr



p = Person(first_name="Oleh", last_name="Andrus", email="asdasdasds")
print(p)