from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator

app = FastAPI()


# Sub-model: Address
class Address(BaseModel):
    city: str
    zip_code: str = Field(..., regex=r"^\d{5}$")


# Sub-model: Item
class Item(BaseModel):
    id: int
    name: str
    price: float
    tags: List[str] = []
    metadata: Optional[Dict[str, Union[str, int]]] = None

    @validator("price")
    def must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        return value


# Main input model: Order
class Order(BaseModel):
    order_id: str
    items: List[Item]
    shipping_address: Address
    expedited: Optional[bool] = False

    @property
    def total(self) -> float:
        return sum(item.price for item in self.items)


# Response model
class OrderSummary(BaseModel):
    order_id: str
    item_count: int
    total_price: float
    shipping_city: str
    expedited: bool


@app.post("/orders/", response_model=OrderSummary)
def submit_order(order: Order):
    if not order.items:
        raise HTTPException(
            status_code=400, detail="Order must contain at least one item."
        )

    summary = OrderSummary(
        order_id=order.order_id,
        item_count=len(order.items),
        total_price=order.total,
        shipping_city=order.shipping_address.city,
        expedited=order.expedited or False,
    )
    return summary
