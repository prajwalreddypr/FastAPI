from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': "Title One", "author": "Author One", "category": "fiction"},
    {'title': "Title two", "author": "Author two", "category": "romace"},
    {'title': "Title three", "author": "Author three", "category": "non fiction"},
    {'title': "Title four", "author": "Author four", "category": "biography"},
    {'title': "Title five", "author": "Author five", "category": "Horror"}
]



# @app.get("/books")
# async def read_all_books():
#     return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book