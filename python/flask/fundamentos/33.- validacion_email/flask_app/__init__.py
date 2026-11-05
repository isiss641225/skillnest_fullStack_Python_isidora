from flask import Flask

app = Flask(__name__)

# Necesaria para utilizar flash() y session.
app.secret_key = "7125b5602f486d49093ffa1a65a780b3251b98a7156e641f"