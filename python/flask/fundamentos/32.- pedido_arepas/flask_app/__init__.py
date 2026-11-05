from flask import Flask

app = Flask(__name__)

# Necesaria para que Flask pueda utilizar flash().
app.secret_key = "586155dc66e2eaeb59ac461458814cec1a993991d8db8562"