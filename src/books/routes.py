from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from .book_data import books
from typing import List
from .schemas import Book,BookUpdateModel

book_router=APIRouter()


@book_router.get("/")
def root():
    return {"message":"hello from root"}

@book_router.get("/books",response_model=List[Book])
async def get_all_books():
    return books


@book_router.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book=book_data.model_dump()
    books.append(new_book)
    return {"message":"book created successfully","book":new_book}

@book_router.get("/books/{book_id}")
async def get_book_by_id(book_id:int)->dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")


@book_router.patch("/books/{book_id}")
async def update_book_by_id(book_id:int,book_update_data:BookUpdateModel)->dict:
    for book in books:
        if book["id"]==book_id:
            book["title"]=book_update_data.title if book_update_data.title else book["title"]
            book["author"]=book_update_data.author if book_update_data.author else book["author"]
            book["publisher"]=book_update_data.publisher if book_update_data.publisher else book["publisher"]
            book["page_count"]=book_update_data.page_count if book_update_data.page_count else book["page_count"]
            book["language"]=book_update_data.language if book_update_data.language else book["language"]
            return {"message":"book updated successfully","book":book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")

@book_router.delete("/books/{book_id}")
async def delete_book_by_id(book_id:int)->dict:
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            return {"message":"book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")