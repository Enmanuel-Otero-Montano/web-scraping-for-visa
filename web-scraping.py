import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

from email.message import EmailMessage
import smtplib
from decouple import config

email_emisor = "oteromontanoenmanuel@gmail.com"
email_contraseña = config("TOKEN_GMAIL")
email_receptor = "ysuarezoquendo@gmail.com"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

asunto = "Prueba"

cuerpo = "Prueba enviada con Python"

email = EmailMessage()
email["From"] = email_emisor
email["To"] = email_receptor
email["Subject"] = asunto
email.set_content(cuerpo)

context = ssl.create_default_context()

url = "https://tramites.migracion.gob.pa/portal_migracion_digital/views/visa_cuba2.php"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup("a")

if len(tags) != 10:
    print("hay un cambio en la página")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_emisor, email_contraseña)
        smtp.sendmail(email_emisor, email_receptor, email.as_string())
else:
    print("todo está igual")

for tag in tags:
    print(tag.get("href", None))