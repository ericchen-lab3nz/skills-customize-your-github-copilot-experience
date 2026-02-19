# Starter Code for FastAPI REST API Assignment

# 1. Install FastAPI and Uvicorn:
#    pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example resource model
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory storage
books: List[Book] = []

# TODO: Add root endpoint
# @app.get("/")
# def read_root():
#     ...

# TODO: Implement CRUD endpoints for Book
# - GET /books
# - GET /books/{id}
# - POST /books
# - PUT /books/{id}
# - DELETE /books/{id}
