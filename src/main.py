from fastapi import FastAPI
from src.books.routes import book_router

app=FastAPI(
    title="bookly",
    description="A simple book management API built with FastAPI",
)
app.include_router(book_router,prefix="/api/v1",tags=["books"])
