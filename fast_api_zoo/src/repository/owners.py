from sqlalchemy.orm import Session

from src.database.models import Owner
from src.schemas.owners import OwnerModel


async def get_owners(db: Session):
    owners = db.query(Owner).all()
    return owners


async def get_owner_by_id(owner_id: int, db: Session):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    return owner


async def get_owner_by_email(email: str, db: Session):
    owner = db.query(Owner).filter_by(email=email).first()
    return owner


async def create_owner(body: OwnerModel, db: Session):
    owner = Owner(**body.model_dump())
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner

