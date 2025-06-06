from typing import List

from fastapi import Depends, HTTPException, status, Path, APIRouter
from sqlalchemy.orm import Session

from src.schemas.owners import OwnerModel, OwnerResponse
from src.database.db import get_db
from src.repository.owners import get_owners, get_owner_by_id, get_owner_by_email, create_owner

router = APIRouter(prefix="/owners", tags=['owners'])

@router.get("/", response_model=List[OwnerResponse], name="Повернути власників")
async def get_owners_list(db: Session = Depends(get_db)):
    owners = await get_owners(db)
    return owners


@router.get("/{owner_id}", response_model=OwnerResponse)
async def get_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = await get_owner_by_id(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.post("/", response_model=OwnerResponse, status_code=status.HTTP_201_CREATED)
async def save_owner(body: OwnerModel, db: Session = Depends(get_db)):
    owner = await get_owner_by_email(body.email, db)
    if owner:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is exists!')

    owner = await create_owner(body, db)
    return owner