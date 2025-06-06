from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from src.database.connect import get_db
from sqlalchemy.orm import Session
from src.database.models import Owner
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from src.settings.base import HASH_ALGORITHM, HASH_SECRET

class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)
    

async def create_access_token(data: dict, expires_delta = 3600):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, HASH_SECRET, algorithm=HASH_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
                           db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode JWT
        payload = jwt.decode(token.credentials, HASH_SECRET, algorithms=[HASH_ALGORITHM])
        email = payload["sub"]
        if email is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception

    user: Owner | None = db.query(Owner).filter(Owner.email == email).first()
    if user is None:
        raise credentials_exception
    return user
