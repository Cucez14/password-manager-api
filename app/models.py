from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.database import Base  # Import Base z database.py

class PasswordEntry(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    site = Column(String, index=True)
    username = Column(String)
    password = Column(String)

class PasswordEntryCreate(BaseModel):
    site: str
    username: str
    password: str
