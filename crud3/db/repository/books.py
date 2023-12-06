from sqlalchemy.orm import Session
from schemas.books import BookCreate
from db.models.books import Book

# creating new book
def create_new_book(book: BookCreate, db: Session):
    book_object= Book(
        title=book.title,
        author=book.author,
        description=book.description,
        rating=book.rating
    )
    db.add(book_object)
    db.commit()
    db.refresh(book_object)
    return book_object

# display books
def list_books(db: Session):
    books = db.query(Book).all()
    return books