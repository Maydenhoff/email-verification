from fastapi import FastAPI
from config.db import engine, Base
from router.user import user_router
# from config.email import enviar_mail
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title= "Mi aplicacion"

app.include_router(user_router)


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

