from flask import Flask

app = Flask(__name__)

# Necesaria para utilizar mensajes flash.
app.secret_key = "7b02105ad43fc3121a794dcec7738cdf8b8e1e17d2b7dcdc"