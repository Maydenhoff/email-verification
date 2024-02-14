from fastapi import APIRouter
from config.db import Session
from schemas.user import User
from services.user import UserService
from fastapi.responses import JSONResponse, Response, ORJSONResponse

user_router = APIRouter()

@user_router.post("/register", tags=["User"])
def register(user: User):
    db = Session()
    if len(user.name) < 1 and not len(user.last_name) < 1 and not len(user.email) < 1 and not len(user.password) < 1 and not len(user.user_name) <1:
        return JSONResponse(status_code=404, content={"message": "Faltan datos"})
    response = UserService(db).register_user(user)
    return JSONResponse(status_code=200, content={"message": response})

@user_router.get("/activate/", tags=["User"])
def activate(cod:str, id:str):
    print("llege")
    db = Session()
    result = UserService(db).activate_user(cod, id)
    print(result)
    return JSONResponse(status_code=200, content={"message": result})

    
@user_router.get("/", tags=["User"])
def get_by_id(id:int):
    db = Session()
    user = UserService(db).get_by_id(id)
    print(type(id))

    if user:

        user_dict = {
            "id": user.id,
            "name": user.name,
            "last_name": user.last_name,
            "user_name": user.user_name,
            "email": user.email,
            "password": user.password,
            "cod": user.cod,
            "validation": user.validation,
            
        }

        return JSONResponse(status_code=200, content={"result": user_dict})
    else:
        return JSONResponse(status_code=404, content={"error": "Usuario no encontrado"})

        