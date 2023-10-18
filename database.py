from sqlmodel import create_engine
from sqlmodel import Session
import os


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn_str='sqlite:///'+os.path.join(BASE_DIR,'maint.db')
print(conn_str)

engine=create_engine(conn_str,echo=True,connect_args = {"check_same_thread" : False})


def get_session():
    with Session(engine) as session:
        yield session