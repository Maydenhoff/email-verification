import os
from dotenv import load_dotenv
import ssl
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_mail( email_reciver, name, subject, cod, id):
    id = str(id)
    load_dotenv()
    password = os.getenv("password")
    email_sender = os.getenv("email_sender")

    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = email_reciver
    msg["Subject"] = subject
    # msg.set_content(body)
    with open("email.html", "r") as archivo:
        html = archivo.read()
    
    html = html.replace("{{id}}", id)
    html = html.replace("{{cod}}", cod)
    html = html.replace("{{email}}", email_reciver)
    html = html.replace("{{nombre}}", name)
   

    msg.attach(MIMEText(html, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_sender, password)

    server.sendmail(
        email_sender,
        email_reciver,
        msg.as_string()
    )

    server.quit()
    
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    #     smtp.login(email_sender, password)
    #     smtp.sendmail(email_sender,email_reciver, em.as_string())


def mail_register(email_reciver, name, cod, id):
    subject = "Bienvenido/a"
    print(id)
    # body= """"
    # HTML
    # <h1>Hola </h1>"""
    enviar_mail(email_reciver, name, subject, cod, id)

