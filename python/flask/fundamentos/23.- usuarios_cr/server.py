from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

# 1. READ ALL
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)

# 2. CREATE FORM
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")

# 3. CREATE PROCESS
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(data)
    return redirect(url_for("usuarios"))

# ==================== NUEVAS RUTAS ====================

# 4. READ ONE (Ver detalle)
@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("usuario.html", usuario=usuario)

# 5. UPDATE FORM (Mostrar formulario de edición)
@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("usuario_editar.html", usuario=usuario)

# 6. UPDATE PROCESS (Procesar edición)
@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar_usuario(id):
    data = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update(data)
    return redirect(url_for("usuarios"))

# 7. DELETE (Eliminar usuario)
@app.route("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    Usuario.delete(id)
    return redirect(url_for("usuarios"))

if __name__ == "__main__":
    app.run(debug=True)