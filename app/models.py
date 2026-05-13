from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # The Python-level Soft Link
    books = relationship("Book", back_populates="owner")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    rating = Column(Float)
    
    # The Hard Link (Database Level) - notice "users.id" matches the __tablename__
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # The Python-level Soft Link
    owner = relationship("User", back_populates="books")