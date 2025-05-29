from pydantic import BaseModel

class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0
    radius: int = 1
    name: str | None = None

c1 = Circle(radius=2, name="A")
print(c1.model_fields_set)

print(Circle.model_fields.keys() - c1.model_fields_set)
