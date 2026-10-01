# ==========================================================
# SERVIDOR FLASK - CONTROLADOR PRINCIPAL
# ==========================================================

# Importamos Flask, render_template, request (para leer formularios) y redirect (para redirigir)
from flask import Flask, render_template, request, redirect
from mascota import Mascota

app = Flask(__name__)


# ----------------------------------------------------------
# RUTA PRINCIPAL: Muestra la lista de mascotas y el formulario
# ----------------------------------------------------------
@app.route("/")
def index():
    # Obtiene todas las mascotas desde la base de datos
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)


# ----------------------------------------------------------
# RUTA FILTRO: Muestra mascotas filtradas por tipo (Ej: /mascotas/Perro)
# ----------------------------------------------------------
@app.route("/mascotas/<tipo>")
def mascotas_por_tipo(tipo):
    mascotas = Mascota.get_by_type(tipo)
    return render_template("index.html", mascotas=mascotas)


# ----------------------------------------------------------
# RUTA DETALLE: Muestra una mascota específica por su ID
# ----------------------------------------------------------
@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    mascota = Mascota.get_by_id(id)
    
    if mascota is None:
        return "Mascota no encontrada", 404
        
    return render_template("mascota.html", mascota=mascota)


# ----------------------------------------------------------
# RUTA CREAR: Procesa el formulario enviando datos por POST
# ----------------------------------------------------------
@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    """
    Recibe los datos del formulario mediante request.form
    y los envía al método save() de la clase Mascota.
    """
    # Creamos un diccionario con los datos ingresados en los inputs
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"]
    }

    # Guardamos el nuevo registro en MySQL
    Mascota.save(datos)

    # Redirigimos al inicio para refrescar la lista
    return redirect("/")


# ----------------------------------------------------------
# EJECUCIÓN DE LA APLICACIÓN
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)