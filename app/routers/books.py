from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Book
from database import get_db
from schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])
#lets use book.modeldump 
@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

@router.get("/", response_model=list[BookResponse])
async def read_books(db: AsyncSession = Depends(get_db)):
    books = await db.execute(select(Book))
    return books.scalars().all()

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)):
    db_book = await db.execute(select(Book).filter(Book.id == book_id))
    db_book = db_book.scalar_one_or_none()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author
    if book.rating is not None:
        db_book.rating = book.rating
    await db.commit()
    await db.refresh(db_book)
    return db_book

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await db.execute(select(Book).filter(Book.id == book_id))
    book = book.scalar_one_or_none()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    await db.delete(book)
    await db.commit()
    return {"message": "Book deleted successfully"}