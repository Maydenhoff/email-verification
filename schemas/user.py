from pydantic import BaseModel

class User(BaseModel):
    name: str
    last_name: str
    user_name: str
    email: str
    password: str
    cod: str = None
    validation: str = None
    fecha_limite: str = None
    


    class Config:
        json_schema_extra = {
            "example":{
                "name": "Mayra",
                "last_name": "Denhoff",
                "user_name": "maydenhoff",
                "email": "mayradenhoff@gmail.com",
                "password": "password"
            }
        }