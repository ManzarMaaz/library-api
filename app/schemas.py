from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title : str
    author : str
    rating : Optional[float] = None
    owner_id : int

class BookResponse(BaseModel):
    id : int
    title : str
    author : str
    rating : Optional[float] = None
    owner_id : int
    model_config = {"from_attributes": True}

class BookUpdate(BaseModel):
    title : Optional[str] = None
    author : Optional[str] = None
    rating : Optional[float] = None

class UserCreate(BaseModel):
    email : str
    password : str

class UserResponse(BaseModel):
    id : int
    email : str
    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    email : Optional[str] = None
    password : Optional[str] = None