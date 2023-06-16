from pydantic import BaseModel


class UserEntity(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CreateUserEntity(BaseModel):
    name: str
