from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_book_by_category(category: str):
    books_to_return = [
        book for book in BOOKS
        if book["category"].casefold() == category.casefold()
    ]
    return books_to_return


@app.get("/books/byauthor/")
async def read_author_category_by_path(author: str, category: str):
    books_to_return = [
        book for book in BOOKS
        if book["author"].casefold() == author.casefold() and book["category"].casefold() == category.casefold()
    ]
    return books_to_return


@app.get("/books/{author_name}")
async def read_author_category_by_query(author_name: str, category: str):
    books_to_return = [
        book for book in BOOKS
        if book["author"].casefold() == author_name.casefold() and book["category"].casefold() == category.casefold()
    ]
    return books_to_return


@app.post("/books/create_body")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
