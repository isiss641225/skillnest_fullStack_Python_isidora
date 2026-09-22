from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
   {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
   {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
   {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
   {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
   {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
   {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
   {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]

# Ruta para mostrar la tabla con datos
@app.route("/rutas")
def ver_todos():
    return render_template("tabla.html", lista=datos, total=len(datos))

if __name__ == "__main__":
   app.run(debug=True)