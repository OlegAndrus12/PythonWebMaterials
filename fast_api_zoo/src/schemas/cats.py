
from pydantic import BaseModel, Field
from src.schemas.owners import OwnerResponse

class CatModel(BaseModel):
    nickname: str = Field('Mur4ik', min_length=3, max_length=16)
    age: int = Field(1, ge=0, le=30)
    vaccinated: bool = False
    description: str
    owner_id: int = Field(1, gt=0)


class CatResponse(BaseModel):
    id: int = 1
    nickname: str
    age: int
    vaccinated: bool
    description: str
    owner: OwnerResponse

    class Config:
        from_attributes = True
