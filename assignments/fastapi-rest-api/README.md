# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple RESTful API using the FastAPI framework in Python. You will create endpoints to manage a collection of resources, handle requests and responses, and test your API locally.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Install FastAPI and Uvicorn, and create a basic FastAPI application with a root endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (use `pip`)
- Create a Python file with a FastAPI app instance
- Add a root endpoint (`/`) that returns a welcome message


### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Add endpoints to create, read, update, and delete items in a simple in-memory list (e.g., books, tasks, or users).

#### Requirements
Completed program should:

- Define a Pydantic model for your resource (e.g., Book)
- Implement endpoints for:
  - GET all items
  - GET item by ID
  - POST (create) a new item
  - PUT (update) an item by ID
  - DELETE an item by ID
- Return appropriate status codes and error messages

---

Use the provided `starter-code.py` to begin. Test your API using a tool like curl, httpie, or the built-in FastAPI docs at `/docs`.
