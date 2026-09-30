from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

# Ruta principal (Todas las mascotas)
@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

# Ruta por tipo (Ej: /mascotas/Perro)
@app.route("/mascotas/<tipo>")
def mascotas_por_tipo(tipo):
    mascotas = Mascota.get_by_type(tipo)
    return render_template("index.html", mascotas=mascotas)

# Ruta por ID (Ej: /mascota/1)
@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    mascota = Mascota.get_by_id(id)
    
    if mascota is None:
        return "Mascota no encontrada", 404
        
    return render_template("mascota.html", mascota=mascota)

if __name__ == "__main__":
    app.run(debug=True)