from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db



@asynccontextmanager
async def life_span(app:FastAPI):
    print("app is starting")
    await init_db()
    yield
    print("app is shutting down")


app=FastAPI(
    title="bookly",
    description="A simple book management API built with FastAPI",
    lifespan=life_span
)
app.include_router(book_router,prefix="/api/v1",tags=["books"])
