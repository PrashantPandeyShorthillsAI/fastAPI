from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Book(Base):
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    author=Column(String)
    description=Column(String)
    rating = Column(Integer)