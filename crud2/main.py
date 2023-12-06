from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def get_all_data():
    return db

# post 
db={}

class Item(BaseModel):
    name:str
    description: str

@app.post("/")
def create(item: Item):
    db[item.name] = item.description
    return {"item": item}

@app.delete("/")
def delete_data(name: str):
    del db[name]
    return db

@app.put("/")
def update_data(item: Item):
    db[item.name] = item.description
    return db