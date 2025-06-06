from pydantic import BaseModel, EmailStr, Field


class OwnerModelRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class OwnerModel(BaseModel):
    email: EmailStr
    password: str
    


class ResponseOwner(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        from_attributes = True

