from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': "Title One", "author": "Author One", "category": "fiction"},
    {'title': "Title two", "author": "Author two", "category": "romace"},
    {'title': "Title three", "author": "Author three", "category": "nonfiction"},
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
        
@app.get("/books/")
def read_catergory_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



@app.get("/books/{book_author}/")

def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return