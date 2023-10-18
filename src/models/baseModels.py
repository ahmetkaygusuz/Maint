from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlmodel import Field, Column,SQLModel


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(default=datetime.now())
    modified: datetime = Field(default=datetime.now())

    modified: datetime = Field(default=datetime.now(),
        sa_column=Column(DateTime(), onupdate=datetime.now()))
    
    passive: bool = Field(default=False)
  