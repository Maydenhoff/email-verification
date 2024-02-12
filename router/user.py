from fastapi import APIRouter
from config.db import Session
from schemas.user import User
from services.user import UserService
from fastapi.responses import JSONResponse
user_router = APIRouter()

@user_router.post("/register", tags=["User"])
def register(user: User):
    db = Session()
    if len(user.name) < 1 and not len(user.last_name) < 1 and not len(user.email) < 1 and not len(user.password) < 1 and not len(user.user_name) <1:
        return JSONResponse(status_code=404, content={"message": "Faltan datos"})
    UserService(db).register_user(user)
    return JSONResponse(status_code=200, content={"message": "Se ha registrado exitosamente"})


    