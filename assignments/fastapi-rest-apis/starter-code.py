from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    summary: str

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    summary: str

books: List[Book] = [
    Book(id=1, title="The Winds of Python", author="A. Coder", year=2024, summary="A beginner's guide to building APIs."),
    Book(id=2, title="FastAPI Fundamentals", author="Dev Expert", year=2025, summary="Learn how to build fast web APIs with Python."),
]

@app.get("/books", response_model=List[Book])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book_create: BookCreate):
    next_id = max((book.id for book in books), default=0) + 1
    new_book = Book(id=next_id, **book_create.dict())
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookCreate):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_update.dict())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
