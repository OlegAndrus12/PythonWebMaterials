
from datetime import datetime
from pydantic import BaseModel, ValidationError
from typing import List
from faker import Faker
from pprint import pprint

def get_mocked_order():
    fake = Faker()

    mock = {
        "order_id": "10",
        "email_address": fake.email(),
        "checkout_date": fake.date(),
        "phone_number": fake.phone_number(),
        "tags": fake.words(),
    }
    return mock


class Order(BaseModel):
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]

    def call_user(self):
        pass

# lax (default)
# strict

# __str__, __repr__
try:
    order = Order(**get_mocked_order())
except ValidationError as e:
    pprint(e, indent=4)

ser_order = order.model_dump_json(indent=4, include=["phone_number", "order_id"], exclude=["order_id"])
print(ser_order)