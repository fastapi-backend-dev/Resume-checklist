from fastapi import FastAPI

import models.user
import models.expense
from core.db import Base, engine
from routers.expense import expense_router
from routers.user import user_router

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(expense_router)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
