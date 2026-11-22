# ---------------------------------------------------------------
# DATABASE SETUP - EASY EXPLANATION
# ---------------------------------------------------------------
# Think of this file as the "database manager" for the FastAPI app.
#
# create_engine:
#     Creates the main connection to the database.
#     Analogy: It is like the "road" that allows Python to travel to
#     and from the database. Engine also manages database connections.
#
# declarative_base:
#     Creates the main Python "base class" for database models.
#     Analogy: It is like a blank workbook or a common blueprint.
#     Models such as Todos(Base) inherit from this class, so SQLAlchemy
#     knows that those classes represent database tables.
#
# sessionmaker:
#     Creates a class/factory that makes database sessions.
#     Analogy: An engine is the road, while a session is one trip on
#     that road. Each request can get its own session from SessionLocal.
#
# connect_args and "check_same_thread":
#     connect_args contains special settings for the database driver.
#     SQLite normally allows a database connection to be used only by
#     the same thread that created it. FastAPI can handle work using
#     multiple threads, so this setting allows the connection to be
#     shared across threads. We set "check_same_thread" to False to
#     prevent a false "you are using another thread" error in FastAPI.
#     Analogy: It allows one database file to receive help from several
#     workers instead of only the original worker.
#
# autocommit vs autoflush:
#     autocommit=False means changes are NOT saved automatically.
#     The code must explicitly call db.commit() to save them.
#     autoflush=False means SQLAlchemy does NOT automatically send
#     pending changes to the database before a query.
#     Analogy: autocommit=False is like an exam answer that is not
#     submitted until we press Submit (db.commit()). autoflush=False
#     means the page is not sent to the teacher before we explicitly
#     ask to read or submit; this gives us more control.
#
# bind:
#     Tells a session which engine/database it must use.
#     Analogy: It is like giving a worker the address of the correct
#     database office. Here, bind=engine makes every SessionLocal
#     session connect through our SQLite engine.
#
# Base:
#     The parent class used to define database table models.
#     Analogy: Base is the master form, and models such Todos(Base)
#     create their own filled-in table forms from it.
# ---------------------------------------------------------------

# Import SQLAlchemy's engine function.
# create_engine opens or creates a database connection pathway.
from sqlalchemy import create_engine

# Import declarative_base().
# It creates the parent class used by Python classes that represent tables.
from sqlalchemy.ext.declarative import declarative_base

# Import sessionmaker().
# It creates the SessionLocal factory used to make individual DB sessions.
from sqlalchemy.orm import sessionmaker

# The database address for SQLAlchemy.
# sqlite:/// means "use SQLite"; ./todos.db means the database file is
# located in the project's current folder and is named todos.db.
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Create the engine that connects this application to the SQLite database.
# SQLite normally checks that a connection is used only by its creating thread.
# FastAPI may use different threads, so check_same_thread=False disables that
# SQLite-only restriction. This setting is safe for this simple app when one
# connection/session is used by one request at a time.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Create a session factory named SessionLocal.
# The factory does not create the database or an immediate session; it defines
# how future sessions will be created.
#
# autocommit=False:
#     Changes stay in the session until db.commit() is called.
#
# autoflush=False:
#     Pending changes are not automatically sent to SQLite before a query.
#
# bind=engine:
#     Every session made by SessionLocal is connected to our SQLite engine.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create Base, the shared parent class for all SQLAlchemy database models.
# For example, class Todos(Base) will become a database table definition.
Base = declarative_base()
