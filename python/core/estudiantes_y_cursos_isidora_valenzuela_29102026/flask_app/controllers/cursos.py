from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.curso import Curso

@app.route("/")
def inicio():
    return redirect(url_for("cursos"))

@app.route("/cursos")
def cursos():
    todos_los_cursos = Curso.get_all()
    return render_template("cursos.html", cursos=todos_los_cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    nombre = request.form.get("nombre", "").strip()
    if nombre:
        Curso.save({"nombre": nombre})
    return redirect(url_for("cursos"))

@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    curso = Curso.get_curso_con_estudiantes(id)
    if not curso:
        return redirect(url_for("cursos"))
    return render_template("mostrar_curso.html", curso=curso)