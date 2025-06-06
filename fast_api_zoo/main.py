from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text


from src.database.db import Base, engine, get_db
from src.routers import cats, owners, auth

app = FastAPI()

@app.on_event("startup")
async def create_tables():
    Base.metadata.create_all(bind=engine)


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")

app.include_router(owners.router, prefix="/api")
app.include_router(cats.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
