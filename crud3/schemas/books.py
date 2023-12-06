from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=1000)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1,lt=101)
    