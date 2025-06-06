from pydantic import BaseModel, Field
from .owners import ResponseOwner

class CatModel(BaseModel):
    nickname: str = Field('Barsik', min_length=3, max_length=12)
    age: int = Field(1, ge=0, le=30)
    vaccinated: bool = False
    description: str
    owner_id: int = Field(1, gt=0)


class CatStatusVaccinated(BaseModel):
    vaccinated: bool


class ResponseCat(BaseModel):
    id: int = 1
    nickname: str
    age: int
    vaccinated: bool
    description: str
    owner: ResponseOwner

    class Config:
        from_attributes = True
