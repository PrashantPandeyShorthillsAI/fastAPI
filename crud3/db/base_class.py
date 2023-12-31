from typing import Any
from sqlalchemy.ext.declarative import declared_attr, as_declarative

@as_declarative()
class Base():
    id:Any
    __name__: str

    # to generate table for classname
    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()