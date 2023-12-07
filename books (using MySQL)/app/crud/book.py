from sqlalchemy.orm import Session
from app.models.book import Book

def create_book(db: Session, name: str, author: str, description: str, rating: float):
    db_book = Book(name=name, author=author, description=description, rating=rating)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, name: str, author: str, description: str, rating: float):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        if name is not None:
            db_book.name = name
        if author is not None:
            db_book.author = author
        if description is not None:
            db_book.description = description
        if rating is not None:
            db_book.rating = rating
        
        db.commit()
        db.refresh(db_book)
        return db_book

    return None

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return db_book
    return None