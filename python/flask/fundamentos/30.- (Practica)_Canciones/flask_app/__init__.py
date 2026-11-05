from flask import Flask

app = Flask(__name__)

# Necesaria para utilizar mensajes flash.
# En un proyecto real la clave debe mantenerse fuera del código.
app.secret_key = "e24db24db1dbfa445319163bbf3f8883d644b486f8c86f1"