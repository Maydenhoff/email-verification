from config.db import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class User(Base):
    __tablename__ = "user"

    id =Column(Integer, primary_key = True, autoincrement=True  )
    name = Column(String)
    last_name = Column(String)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    cod = Column(String)
    validation = Column(Boolean, default= False)
    fecha_limite = Column(DateTime)

