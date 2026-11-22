# ---------------------------------------------------------------
# EXPLANATION OF Todos(Base)
# ---------------------------------------------------------------
# Todos(Base) means that the Python class named Todos inherits from
# Base, which is the common database parent class created in database.py.
#
# Easy analogy:
#     Base is like a master registration form for database tables.
#     Todos(Base) is like a filled registration form for one specific
#     table. It tells SQLAlchemy: "Create a table named todos."
#
# More simply:
#     Base provides the SQLAlchemy database-table features.
#     Todos receives those features because it inherits from Base.
#     __tablename__ = "todos" gives the table its real SQLite name.
#     Each Todo object is one row in the todos table.
#     id, title, description, priority, and completed are table columns.
#
# A real-life example:
#     Todos is like an empty student-register template.
#     One Todos object is like one completed row about one student.
#     The row stores title, description, priority, and completion status.
#
# When SQLAlchemy creates the table:
#     Todos(Base) registers the Python class as a database model.
#     __tablename__ decides the table name: todos.
#     Column(...) defines each field that belongs to a row.
# ---------------------------------------------------------------

from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
