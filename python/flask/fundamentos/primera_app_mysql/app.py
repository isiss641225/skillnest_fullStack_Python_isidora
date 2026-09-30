# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================

from flask import Flask, render_template
from mascota import Mascota

# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """
    mascotas = Mascota.get_all()
    print(mascotas)

    # Corregido: 'todas_mascotas' para que coincida con el HTML
    return render_template(
        "index.html",
        todas_mascotas=mascotas
    )


# ==========================================================
# RUTA: FILTRAR SOLO PERROS
# ==========================================================

@app.route("/mascotas/perros")
def perros():
    """
    Consulta únicamente las mascotas cuyo tipo sea 'Perro'.
    """
    solo_perros = Mascota.get_by_type("Perro")

    # Corregido: se pasa solo_perros a la variable todas_mascotas
    return render_template(
        "index.html",
        todas_mascotas=solo_perros
    )


# ==========================================================
# EJECUTAR SERVIDOR (Siempre al final del archivo)
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)