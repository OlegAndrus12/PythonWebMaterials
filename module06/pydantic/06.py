
from datetime import datetime
from pydantic import BaseModel
from typing import List
from pprint import pprint

class Order(BaseModel):
    order_id: int = 0
    email_address: str
    checkout_date: datetime = ""
    phone_number: str = ""
    tags: List[str]

class OrdersList(BaseModel):
    list_name: str
    date: str
    orders: List[Order]


pprint(OrdersList.model_json_schema())