from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.crud.book import create_book, delete_book, get_books, get_book, update_book
from app.models.book import Book as BookModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books/")
def create_book_endpoint(name: str, author: str, description: str, rating: float, db: Session = Depends(get_db)):
    return create_book(db, name, author, description, rating)

@router.get("/books/")
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db, skip=skip, limit=limit)

@router.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/books/{book_id}")
def update_book_endpoint(
    book_id: int, name: str = None, author: str = None, description: str = None, rating: float = None, db: Session = Depends(get_db)
):
    updated_book = update_book(db, book_id, name, author, description, rating)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    deleted_book = delete_book(db, book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book