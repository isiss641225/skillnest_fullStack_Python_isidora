from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

# 1. Ruta para MOSTRAR todos los usuarios (READ)
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)

# 2. Ruta para MOSTRAR el formulario de creación
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")

# 3. Ruta para PROCESAR la creación del nuevo usuario (CREATE)
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip()
    }
    
    Usuario.save(data)
    
    # Redirige de vuelta al listado de usuarios
    return redirect(url_for("usuarios"))

if __name__ == "__main__":
    app.run(debug=True)