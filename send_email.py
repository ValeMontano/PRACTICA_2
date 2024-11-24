import smtplib
import ssl
import os

# Configuración del servidor SMTP
port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')

# Información del repositorio y rama
branch_name = os.environ.get('GITHUB_REF', 'Unknown branch').split('/')[-1]
repository = os.environ.get('GITHUB_REPOSITORY', 'Unknown repository')

# Construcción del mensaje
subject = f"Changes pushed to branch: {branch_name}"
body = f"""
Hola,

Se han realizado cambios en la rama '{branch_name}' del repositorio '{repository}'.
Revisa el historial de commits para más detalles.

Saludos,
GitHub Actions
"""
message = f"Subject: {subject}\n\n{body}"

# Envío del correo
context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, USERNAME, message)
        print("Correo enviado con éxito.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
