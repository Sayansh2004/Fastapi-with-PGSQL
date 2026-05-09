from pydantic import BaseModel


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