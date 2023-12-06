from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.books import BookCreate
from db.session import get_db
from db.repository.books import create_new_book
 
router = APIRouter()

@router.post("/")
def create_new_book(book: BookCreate,db: Session=Depends(get_db)):
    book = create_new_book(book=book, db=db)
    return book

@router.get("/all")
def read_all_books(db:Session = Depends(get_db)):
    books = list(db=db)
    return books