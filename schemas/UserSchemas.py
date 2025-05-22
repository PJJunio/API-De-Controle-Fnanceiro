from pydantic import BaseModel, EmailStr, constr
from uuid import UUID as PythonUUID


class UserCreateInput(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class UserListOutput(BaseModel):
    user_id: int
    email: EmailStr

    class Config:
        orm_mode = True

class StandartUserOutput(BaseModel):
    message: str