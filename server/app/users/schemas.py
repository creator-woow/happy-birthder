from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    hashed_password: str
