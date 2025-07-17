from fastapi import FastAPI, HTTPException
from app import models, database, crud
from sqlalchemy.orm import Session
from fastapi import Depends

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Password Manager API je spustené!"}

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/passwords")
def read_passwords(db: Session = Depends(get_db)):
    return crud.get_passwords(db)

@app.post("/passwords")
def create_password(entry: models.PasswordEntryCreate, db: Session = Depends(get_db)):
    return crud.create_password(db, entry)

@app.put("/passwords/{password_id}")
def update_password(password_id: int, entry: models.PasswordEntryCreate, db: Session = Depends(get_db)):
    return crud.update_password(db, password_id, entry)

@app.delete("/passwords/{password_id}")
def delete_password(password_id: int, db: Session = Depends(get_db)):
    return crud.delete_password(db, password_id)

# Tento riadok je len na otestovanie CI pipeline
