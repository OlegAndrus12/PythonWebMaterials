from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session

from src.database.connect import get_db
from src.schemas.cats import ResponseCat, CatModel, CatStatusVaccinated
from src.repository import cats as repository_cats
from src.repository.auth import get_current_user

router = APIRouter(prefix='/cats', tags=['cats'], dependencies=[Depends(get_current_user)] )


@router.get("/", response_model=List[ResponseCat])
async def get_cats(query: str = "", limit: int = Query(10, le=1000), offset: int = 0, owner_id: int = None, is_vaccinated: bool = None,
                   db: Session = Depends(get_current_user)):
    cats = await repository_cats.get_cats(limit, offset, owner_id, is_vaccinated, db)
    return cats


@router.get("/{cat_id}", response_model=ResponseCat,)
async def get_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = await repository_cats.get_cat(cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.post("/", response_model=ResponseCat, status_code=status.HTTP_201_CREATED)
async def create_cat(body: CatModel, db: Session = Depends(get_db)):
    cat = await repository_cats.create_cat(body, db)
    return cat


@router.put("/{cat_id}", response_model=ResponseCat)
async def update_cat(body: CatModel, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = await repository_cats.update_cat(body, cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.patch("/{cat_id}", response_model=ResponseCat)
async def update_cat(body: CatStatusVaccinated, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = await repository_cats.update_vaccinated_cat(body, cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.delete("/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = await repository_cats.remove_cat(cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat
