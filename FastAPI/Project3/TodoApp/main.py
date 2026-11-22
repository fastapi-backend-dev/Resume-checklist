# ---------------------------------------------------------------
# EASY EXPLANATION OF DEPENDENCY INJECTION AND REQUEST DATA
# ---------------------------------------------------------------
# Depends:
#     FastAPI uses Depends to call another function automatically.
#     Analogy: A waiter (FastAPI) gives a customer (endpoint) a fresh
#     glass of water (database session) instead of making the customer
#     prepare it. Depends(get_db) means FastAPI will run get_db().
#
# Session vs sessionmaker:
#     sessionmaker is the factory that creates database sessions.
#     SessionLocal = sessionmaker(...) is the factory in database.py.
#     Session is the SQLAlchemy session type used for type hints.
#     db = SessionLocal() is a real session created for one request.
#     Analogy: sessionmaker is a photocopy machine, while one Session
#     is a single photocopy ready to work with. Session describes the
#     shape, and SessionLocal creates the actual working object.
#
# Annotated:
#     Annotated[T, extra_information] adds FastAPI metadata to a type.
#     db_dependency = Annotated[Session, Depends(get_db)] means:
#     "db is a SQLAlchemy Session, and FastAPI must create it using get_db."
#     Analogy: It is like writing "water, COLD" on an order: water is
#     the item, while COLD is extra instruction for how to serve it.
#
# BaseModel:
#     Pydantic BaseModel defines and validates the JSON request body.
#     TodoRequest(BaseModel) creates a form for client input.
#     Analogy: BaseModel is a blank application form. TodoRequest fills
#     that form with fields such as title and completed.
#     If the supplied JSON does not match the rules, FastAPI rejects it.
#
# models.Base.metadata.create_all(bind=engine):
#     This tells SQLAlchemy to read every table model belonging to Base
#     and create missing tables in the connected SQLite database.
#     For this file, it creates the todos table if it does not exist.
#     bind=engine says which database the table should be created in.
#     Analogy: The base is a list of table recipes, engine is the address
#     of the kitchen, and create_all() cooks or creates the missing dishes.
#     It does not replace or duplicate an existing table.
#
# get_db():
#     This is a dependency-generator for database sessions.
#     1. db = SessionLocal() creates a fresh session.
#     2. yield db gives that session to the endpoint.
#     3. FastAPI runs the endpoint with the session.
#     4. finally + db.close() closes the session after the request.
#     Analogy: get_db() is a hotel key desk. It gives one temporary room
#     key (session) to a request and collects it back when the guest leaves.
#
# db_dependency:
#     db_dependency stores a reusable FastAPI annotation.
#     It combines the SQLAlchemy Session type with Depends(get_db).
#     Parameters using db_dependency will automatically receive a session.
#     Analogy: It is a saved shortcut or reusable "request ticket" that
#     says "please provide me a database session."
#
# db: db_dependency:
#     This declares a parameter named db with the db_dependency type.
#     FastAPI detects the dependency and puts a real Session in db.
#     Analogy: It is like writing "deliver a database worker to db."
#     Inside the endpoint, db.query(...), db.add(...), and db.commit()
#     use that working session.
#
# todo_request.model_dump():
#     This converts a validated Pydantic TodoRequest object into a Python
#     dictionary. For example, title and completed become dictionary keys.
#     Analogy: TodoRequest is a filled application form; model_dump()
#     converts it into labeled JSON-like data: {"title": "...", ...}.
#     ** before the dictionary expands its key/value pairs as keyword
#     arguments to the Todos constructor.
#     Result:
#         Todos(**todo_request.model_dump())
#     is similar to:
#         Todos(title=..., description=..., priority=..., completed=...)
# ---------------------------------------------------------------

from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel, Field

import models
from database import engine, SessionLocal
from models import Todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_lenght=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    completed: bool


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found.")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()


@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)
):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found.")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.completed = todo_request.completed

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found.")
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
