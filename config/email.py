import os
from dotenv import load_dotenv
import ssl
import smtplib
from email.message import EmailMessage

def enviar_mail(email_sender, email_reciver, subject, body):
    load_dotenv()
    # print(email_reciver, "ACAAAA")
    # email_sender = "mayradenhoff@gmail.com"
    password = os.getenv("password")
    # email_reciver = "mayradenh@gmail.com"
    # subject = "Suscripcion"
    # body = """
    # esta funcionando
    # """


    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender,email_reciver, em.as_string())
