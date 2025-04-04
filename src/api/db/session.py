import sqlmodel
from sqlmodel import SQLModel
from .config import DATABASE_URL

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL must be set")
engine = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print("Initializing DB")
    SQLModel.metadata.create_all(engine)
