from fastapi import FastAPI
from config.db import engine, Base
from router.user import user_router
from config.email import enviar_mail

# enviar_mail("mayradenhoff@gmail.com", "mayradenh@gmail.com", "Suscripcion")
# Envio mail
# from email.message import EmailMessage
# import os
# from dotenv import load_dotenv
# import ssl
# import smtplib


# load_dotenv()
# email_sender = "mayradenhoff@gmail.com"
# password = os.getenv("password")
# email_reciver = "mayradenh@gmail.com"
# subject = "Suscripcion"
# body = """
# esta funcionando
# """


# em = EmailMessage()
# em["From"] = email_sender
# em["To"] = email_reciver
# em["Subject"] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, password)
#     smtp.sendmail(email_sender,email_reciver, em.as_string())

# hasta aca



app = FastAPI()
app.title= "Mi aplicacion"

app.include_router(user_router)

Base.metadata.create_all(bind=engine)

