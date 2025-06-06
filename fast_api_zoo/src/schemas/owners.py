from pydantic import BaseModel, EmailStr
from datetime import datetime


class OwnerModel(BaseModel):
    email: EmailStr


class OwnerResponse(BaseModel):
    id: int = 1
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
