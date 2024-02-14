from models.user import User as UserModel
import hashlib
import secrets
from datetime import datetime, timedelta
import os
from config.email import mail_register

class UserService():
    def __init__(self, db) -> None:
        self.db = db
        
    def register_user(self, user: UserModel):
        new_user = UserModel(**user.dict())

        result = self.db.query(UserModel).filter(UserModel.email == user.email).first()
        if result:
            if result.validation:
                return "El usuario ya esta registrado"    
            elif not result.validation:
                fecha_actual = datetime.now()
                fecha_nueva = fecha_actual + timedelta(minutes=30)
                random_string = secrets.token_urlsafe(16)
                hashed_string = hashlib.sha256(random_string.encode()).hexdigest()
                result.fecha_limite = fecha_nueva
                result.cod = hashed_string
                self.db.commit()
                mail_register(user.email, user.name, new_user.cod, result.id )

                return "se ha enviado otro codigo"


        #Generar una cadena de caracteres aleatoria
        random_string = secrets.token_urlsafe(16)

        #Calcular el hash sha 256 de la cadena de caracteres aleaotoria
        hashed_string = hashlib.sha256(random_string.encode()).hexdigest()
        new_user.cod = hashed_string
        
        # Poner fecha
        fecha_actual = datetime.now()
        # Le agrego 30 min
        fecha_nueva = fecha_actual + timedelta(minutes=30)

        new_user.fecha_limite = fecha_nueva
        self.db.add(new_user)
        self.db.commit()

        result = self.db.query(UserModel).filter(UserModel.email == new_user.email).first()
        print(result.id)
        mail_register(user.email, user.name, new_user.cod, result.id )
        return "Se ha enviado el codigo"
    

    def activate_user(self, cod, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        # print(result.email)
        print("ENTROO")
        fecha_actual = datetime.now()
        if result.cod == cod and fecha_actual< result.fecha_limite:
            print("eentre al 1")
            result.validation = True
            self.db.commit()
            return "La cuenta ha sido habilitada"
        elif result.cod != cod:
            print("eentre al 2")
            mail_register(result.email, result.name, result.cod, result.id )
            return "El codigo no es el proporcionado, se te reenviara un mail"
        elif result.fecha_limite < fecha_actual:
            print("si lego")
            mail_register(result.email, result.name, result.cod, result.id )
            return "El plazo de tiempo fue superado se te reenviara el mail"
        
            


    def get_by_id(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
