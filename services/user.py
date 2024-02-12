from models.user import User as UserModel
from config.email import enviar_mail
import hashlib
import secrets
from datetime import datetime, timedelta

class UserService():
    def __init__(self, db) -> None:
        self.db = db

    def register_user(self, user: UserModel):
        new_user = UserModel(**user.dict())

        #Generar una cadena de caracteres aleatoria
        random_string = secrets.token_urlsafe(16)

        #Calcular el hash sha 256 de la cadena de caracteres aleaotoria
        hashed_string = hashlib.sha256(random_string.encode()).hexdigest()
        new_user.cod = hashed_string
        new_user.validation = False
        
        # Poner fecha
        fecha_actual = datetime.now()
        # Le agrego 30 min
        fecha_nueva = fecha_actual + timedelta(minutes=30)

        new_user.fecha_limite = fecha_nueva

        # enviar_mail("mayradenhoff@gmail.com", user.email, "Register", "Te llego mi mail o que?")
        self.db.add(new_user)
        self.db.commit()
        return