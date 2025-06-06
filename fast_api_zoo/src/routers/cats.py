from typing import List
from fastapi import Depends, HTTPException, status, Path, APIRouter, Query

from sqlalchemy.orm import Session
from src.schemas.cats import CatResponse, CatModel
from src.database.db import get_db
from src.repository.cats import get_cats, get_cat_by_id, create_cat
from src.services.auth import auth_service
from src.database.models import User
router = APIRouter(prefix="/cats", tags=['cats'])


@router.get("/", response_model=List[CatResponse])
async def get_cats_list(limit: int = Query(10, le=500), offset: int = 0, db: Session = Depends(get_db),
                        _: User = Depends(auth_service.get_current_user)):
    cats = await get_cats(limit, offset, db)
    return cats


@router.get("/{cat_id}", response_model=CatResponse)
async def get_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = await get_cat_by_id(cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.post("/", response_model=CatResponse, status_code=status.HTTP_201_CREATED)
async def save_cat(body: CatModel, db: Session = Depends(get_db)):
    cat = await create_cat(body, db)
    return cat
