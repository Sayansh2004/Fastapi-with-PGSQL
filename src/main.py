from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from typing import List
app=FastAPI()

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "publisher": "Avery",
        "published_date": "2018-10-16",
        "page_count": 320,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 3,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperOne",
        "published_date": "1988-04-15",
        "page_count": 208,
        "language": "Portuguese"
    },
    {
        "id": 4,
        "title": "Deep Work",
        "author": "Cal Newport",
        "publisher": "Grand Central Publishing",
        "published_date": "2016-01-05",
        "page_count": 304,
        "language": "English"
    }
]

class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str

class BookUpdateModel(BaseModel):
    title:str|None
    author:str|None
    publisher:str|None
    page_count:int|None
    language:str|None

@app.get("/")
def root():
    return {"message":"hello from root"}

@app.get("/books",response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book=book_data.model_dump()
    books.append(new_book)
    return {"message":"book created successfully","book":new_book}

@app.get("/books/{book_id}")
async def get_book_by_id(book_id:int)->dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")


@app.patch("/books/{book_id}")
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

@app.delete("/books/{book_id}")
async def delete_book_by_id(book_id:int)->dict:
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            return {"message":"book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")