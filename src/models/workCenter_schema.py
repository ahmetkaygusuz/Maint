
from pydantic import BaseModel, validator


class WorkCenterDTO(BaseModel):
    id:int
    code: str
    name: str


class WorkCenterCreate(BaseModel):
    code: str
    name: str

    @validator('code')
    def checkName(cls, code):
        if len(code) < 5:
            raise ValueError("Code en az 5 karakter olmalı")
        return code