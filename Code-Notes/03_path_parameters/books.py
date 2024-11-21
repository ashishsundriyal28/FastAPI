from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

'''
# Example just to explain chronological order
@app.get("/books/mybook")
async def read_all_books():
    return {'book_title' : "My Favourite Book !!"}
'''


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {'dynamic_param' : dynamic_param}


# To get a specific book title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

