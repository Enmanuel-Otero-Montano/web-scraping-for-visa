from email.message import EmailMessage
import ssl
import smtplib
from decouple import config

email_emisor = "oteromontanoenmanuel@gmail.com"
email_contraseña = config("TOKEN_GMAIL")
email_receptor = "ysuarezoquendo@gmail.com"

asunto = "Prueba"

cuerpo = "Prueba enviada con Python"

email = EmailMessage()
email["From"] = email_emisor
email["To"] = email_receptor
email["Subject"] = asunto
email.set_content(cuerpo)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_emisor, email_contraseña)
    smtp.sendmail(email_emisor, email_receptor, email.as_string())
