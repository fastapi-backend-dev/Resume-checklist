from fastapi import FastAPI, Body, Path, Query, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: str
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="The ID of book is required for update, but not required for create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(ge=1, le=5)
    published_date: int = Field(ge=1900, le=2030)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book title",
                "author": "A new book author",
                "description": "A new book description",
                "rating": 3,
                "published_date": 2025
            }
        }
    }


BOOKS = [
    Book(id=1, title="Complete Guide to FastAPI", author="krishnajangir", description="A comprehensive guide to FastAPI", rating=3, published_date=2021),
    Book(id=2, title="Complete Guide to Django", author="krishnajangir", description="A comprehensive guide to Django", rating=4, published_date=2020),
    Book(id=3, title="Complete Guide to Flask", author="krishnajangir", description="A comprehensive guide to Flask", rating=5, published_date=2018),
    Book(id=4, title="HP1", author="Author 1", description="Book Description", rating=3, published_date=2025),
    Book(id=5, title="HP2", author="Author 2", description="Book Description", rating=4, published_date=2023),
    Book(id=6, title="HP3", author="Author 3", description="Book Description", rating=1, published_date=2021)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int=Path(ge=1)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int=Query(ge=1, le=5)):
    books_to_return = [
        book for book in BOOKS
        if book.rating == rating
    ]
    return books_to_return


@app.get("/books/by_published_date/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date: int=Query(ge=1900, le=2030)):
    books_to_return = [
        book for book in BOOKS
        if book.published_date == published_date
    ]
    return books_to_return


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(get_book_id(new_book))


def get_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book.id} not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int=Path(ge=1)):
    book_changed = False

    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break

    if not book_changed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")
