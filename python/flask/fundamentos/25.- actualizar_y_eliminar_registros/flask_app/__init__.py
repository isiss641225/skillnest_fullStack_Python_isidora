from flask import Flask

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Clave secreta necesaria para manejar sesiones y mensajes flash en Flask
app.secret_key = "clave_secreta_estudiantes"