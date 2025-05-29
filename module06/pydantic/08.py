from pydantic import BaseModel, Field
from faker import Faker

faker = Faker()

class User(BaseModel):
    name: str = Field(default_factory=faker.name)
    email: str = Field(default_factory=faker.email)
    address: str = Field(default_factory=faker.address)


user = User()
print(user)