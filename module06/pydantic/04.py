
from pydantic import BaseModel


class Circle(BaseModel):
    center: tuple[int, int] = (0, 0) # optional
    radius: int # required

c = Circle(radius=1)
print(c)