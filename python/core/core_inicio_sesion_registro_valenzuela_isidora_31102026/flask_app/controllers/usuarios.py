from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def inicio():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    password_encriptada = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],              # Cambiado a 'email'
        "password": password_encriptada,
        "fecha_nacimiento": request.form['fecha_nacimiento']
    }

    usuario_id = Usuario.guardar(datos)
    session['usuario_id'] = usuario_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.obtener_por_email({'email': request.form['email']})
    if not usuario:
        flash("Correo o contraseña incorrectos.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Correo o contraseña incorrectos.", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.obtener_por_id({'id': session['usuario_id']})
    return render_template('dashboard.html', usuario=usuario)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')