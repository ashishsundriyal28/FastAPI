from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(1, "Computer Science pro", "codingwithroby", "a very nice book", 5),
    Book(2, "Be Fast with FastAPI", "codingwithroby", "a great book", 5),
    Book(3, "Master Endpoints", "codingwithroby", "a awsome book", 5),
    Book(4, "HP1", "Author 1", "Book Description", 2),
    Book(5, "HP2", "Author 2", "Book Description", 3),
    Book(6, "HP3", "Author 3", "Book Description", 1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

'''
@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    return BOOKS

'''
@app.post("/create-book")
async def create_book(book_request:BookRequest):
    # print(type(book_request))
    # #BOOKS.append(book_request)
    # ---------------------------------------------------------
    # should use any one
    # i am using model_dump() that is pydantic version 2
    # new_book = Book(**book_request.dict())
    # new_book = Book(**book_request.model_dump())
    # --------------------------------------------------------
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)
    return BOOKS