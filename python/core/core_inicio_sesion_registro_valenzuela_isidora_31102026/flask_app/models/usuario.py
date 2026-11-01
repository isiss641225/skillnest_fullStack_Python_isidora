from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime, date
import re

CORREO_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

class Usuario:
    BASE_DATOS = "esquema_usuarios"

    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.correo = datos['correo']
        self.password = datos['password']
        self.fecha_nacimiento = datos.get('fecha_nacimiento')
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

    @classmethod
    def guardar(cls, datos):
        query = """
        INSERT INTO usuarios (nombre, apellido, correo, password, fecha_nacimiento)
        VALUES (%(nombre)s, %(apellido)s, %(correo)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_por_correo(cls, datos):
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        if len(resultados) < 1:
            return False
        return cls(resultados[0])

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        if len(resultados) < 1:
            return False
        return cls(resultados[0])

    @staticmethod
    def validar_registro(datos_usuario):
        es_valido = True

        if len(datos_usuario['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        elif not NOMBRE_REGEX.match(datos_usuario['nombre']):
            flash("El nombre solo debe contener letras.", "registro")
            es_valido = False

        if len(datos_usuario['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        elif not NOMBRE_REGEX.match(datos_usuario['apellido']):
            flash("El apellido solo debe contener letras.", "registro")
            es_valido = False

        if not CORREO_REGEX.match(datos_usuario['correo']):
            flash("El correo electrónico no es válido.", "registro")
            es_valido = False
        else:
            usuario_existente = Usuario.obtener_por_correo({'correo': datos_usuario['correo']})
            if usuario_existente:
                flash("Este correo electrónico ya está registrado.", "registro")
                es_valido = False

        if len(datos_usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
        elif not PASSWORD_REGEX.match(datos_usuario['password']):
            flash("La contraseña debe incluir al menos una letra mayúscula y un número.", "registro")
            es_valido = False

        if datos_usuario['password'] != datos_usuario['confirmar_password']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False

        if not datos_usuario.get('fecha_nacimiento'):
            flash("Debes ingresar tu fecha de nacimiento.", "registro")
            es_valido = False
        else:
            fecha_nac = datetime.strptime(datos_usuario['fecha_nacimiento'], '%Y-%m-%d').date()
            hoy = date.today()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            if edad < 18:
                flash("Debes tener al menos 18 años para registrarte.", "registro")
                es_valido = False

        return es_valido