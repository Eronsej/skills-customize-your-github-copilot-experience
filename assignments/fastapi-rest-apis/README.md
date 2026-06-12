# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to manage a list of books. Students will learn how to define endpoints, work with request and response models, and handle CRUD operations.

## 🔧 Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## 📝 Tasks

### 🛠️ Define API Models

#### Description
Create Pydantic models for book data and request payloads.

#### Requirements
Completed program should:

- Define a `Book` model with `id`, `title`, `author`, `year`, and `summary` fields.
- Define a `BookCreate` model for creating new books without an `id`.
- Use the models in request and response bodies.

### 🛠️ Create CRUD Endpoints

#### Description
Implement REST endpoints for listing, retrieving, creating, updating, and deleting books.

#### Requirements
Completed program should:

- Provide a `GET /books` endpoint that returns all books.
- Provide a `GET /books/{book_id}` endpoint that returns a single book by ID.
- Provide a `POST /books` endpoint that creates a new book.
- Provide a `PUT /books/{book_id}` endpoint that updates an existing book.
- Provide a `DELETE /books/{book_id}` endpoint that removes a book.

### 🛠️ Run and Test the API

#### Description
Start the FastAPI server, test its endpoints, and verify the responses.

#### Requirements
Completed program should:

- Run using Uvicorn, for example: `uvicorn starter_code:app --reload`
- Return HTTP 404 when a book is not found.
- Use correct response codes for create, update, and delete operations.
- Allow testing with the interactive API docs at `/docs`.
