from fastapi import FastAPI

from users.router import router as user_router
from auth.router import router as auth_router

app = FastAPI()


app.include_router(user_router)
app.include_router(auth_router)
