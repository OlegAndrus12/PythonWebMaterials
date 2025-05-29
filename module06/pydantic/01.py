
from datetime import datetime
from typing import List

import random
from faker import Faker
from dataclasses import dataclass

def get_mocked_order():
    fake = Faker()

    mock = {
        "order_id": 1,
        "email_address": "andrusoleg123gmail.com",
        "checkout_date": fake.date(),
        "phone_number": fake.phone_number(),
        "tags": fake.words(),
    }
    return mock


@dataclass
class Order:
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]
    
    @property
    def order_id(self):
        return self.order_id
    
    @order_id.setter
    def order_id(self, value):
        if isinstance(value, int):
            self.__order_id = value
        else:
            raise TypeError()

order = Order(**get_mocked_order())
print(order)
order.order_id = "asdasds"
print(order.order_id)


# mypy

# pydantic
