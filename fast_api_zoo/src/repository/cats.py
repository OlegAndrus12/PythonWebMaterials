from sqlalchemy.orm import Session

from src.database.models import Cat
from src.schemas.cats import CatModel


async def get_cats(limit: int, offset: int, db: Session):
    cats = db.query(Cat).limit(limit).offset(offset).all()
    return cats


async def get_cat_by_id(cat_id: int, db: Session):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    return cat


async def create_cat(body: CatModel, db: Session):
    cat = Cat(**body.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat