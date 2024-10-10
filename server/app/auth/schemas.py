from pydantic import EmailStr, BaseModel


class AuthSchema(BaseModel):
    email: EmailStr
    password: str
