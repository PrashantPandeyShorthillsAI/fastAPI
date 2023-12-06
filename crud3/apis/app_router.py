from fastapi import FastAPI, APIRouter

page_router = APIRouter()

@page_router.get("/")
async def home():
    return {"msg":"This is homePage"}

@page_router.get("/about")
async def about():
    return {"msg":"This is About Page"}
