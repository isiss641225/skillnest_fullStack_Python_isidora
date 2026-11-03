from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.estudiante import Estudiante

@app.route("/")
@app.route("/estudiantes")
def estudiantes():
    lista_estudiantes = Estudiante.get_all()
    return render_template("estudiantes.html", estudiantes=lista_estudiantes)

@app.route("/estudiantes/ver/<int:id_estudiante>")
def ver_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    return render_template("estudiante_ver.html", estudiante=estudiante)

@app.route("/estudiantes/editar/<int:id_estudiante>")
def editar_estudiante(id_estudiante):
    estudiante = Estudiante.get_by_id(id_estudiante)
    if estudiante is None:
        return "Estudiante no encontrado", 404
    return render_template("estudiante_editar.html", estudiante=estudiante)

@app.route("/actualizar_estudiante", methods=["POST"])
def actualizar_estudiante():
    id_estudiante = request.form["id_estudiante"]
    nombre = request.form["nombre"].strip()
    email = request.form["email"].strip()

    if not nombre or not email:
        estudiante = Estudiante.get_by_id(int(id_estudiante))
        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="Todos los campos son obligatorios."
        )

    data = {
        "id_estudiante": id_estudiante,
        "nombre": nombre,
        "email": email
    }

    resultado = Estudiante.actualizar(data)
    if resultado is False:
        estudiante = Estudiante.get_by_id(int(id_estudiante))
        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="No fue posible actualizar el estudiante."
        )

    return redirect(url_for("estudiantes"))

@app.route("/eliminar_estudiante/<int:id_estudiante>")
def eliminar_estudiante(id_estudiante):
    data = {"id_estudiante": id_estudiante}
    resultado = Estudiante.eliminar(data)
    if resultado is False:
        return "No fue posible eliminar el estudiante.", 500
    return redirect(url_for("estudiantes"))