import smtplib
import ssl
import os

# Configuración del servidor SMTP y credenciales
smtp_server = os.environ.get('SMTP_SERVER')
port = int(os.environ.get('SMTP_PORT', 465))
username = os.environ.get('USER_EMAIL')
password = os.environ.get('USER_PASSWORD')

# Contenido del correo
branch_name = os.environ.get('BRANCH_NAME', 'Unknown Branch')
repository = os.environ.get('REPOSITORY_NAME', 'Unknown Repository')
subject = f"Changes pushed to branch: {branch_name}"
body = f"""
Hola,

Se han realizado cambios en la rama {branch_name} del repositorio {repository}.
Revisa el historial para más detalles.

Saludos,
GitHub Actions
"""
message = f"Subject: {subject}\n\n{body}"

# Conexión y envío
context = ssl.create_default_context()
try:
    print(f"Connecting to SMTP server {smtp_server}:{port}")
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
        print("Correo enviado con éxito")
except smtplib.SMTPException as e:
    print(f"Error al enviar el correo: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
