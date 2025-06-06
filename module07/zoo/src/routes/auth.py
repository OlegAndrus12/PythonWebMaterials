from fastapi import APIRouter, Depends, HTTPException, status, Path, Query

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session

from src.database.connect import get_db
from src.schemas.owners import OwnerModel, OwnerModelRegister
from src.repository import owners as repository_owners
from src.repository.auth import Hash, create_access_token

router = APIRouter(prefix='/auth', tags=['auth'])
hash_handler = Hash()

@router.post("/signup")
async def signup(body: OwnerModelRegister, db: Session = Depends(get_db)):
    owner = await repository_owners.get_owner_by_email(body.email, db)
    if owner:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = hash_handler.get_password_hash(body.password)
    owner = await repository_owners.create_owner(body, db)
    
    return {"email": owner.email}

@router.post("/login")
async def login(body: OwnerModel, db: Session = Depends(get_db)):
    owner = await repository_owners.get_owner_by_email(body.email, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")

    if not hash_handler.verify_password(body.password, owner.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    # Generate JWT
    access_token = await create_access_token(data={"sub": owner.email})
    return {"access_token": access_token, "token_type": "bearer"}

