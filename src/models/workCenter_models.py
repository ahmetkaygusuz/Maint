
from src.models.baseModels import Base

class WorkCenter(Base, table=True):
    code: str
    name: str



   