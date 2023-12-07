from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    author = Column(String(100))
    description = Column(String(100))
    rating = Column(Float)
