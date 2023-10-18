from sqlmodel import SQLModel
from database import engine

print("CREATING DATABASE.....")

SQLModel.metadata.create_all(engine)