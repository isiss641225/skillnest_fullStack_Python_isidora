from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime, date

class Usuario:
    BASE_DATOS = "esquema_usuarios"

    def __init__(self, datos):
        self.id = datos.get('id')
        self.nombre = datos.get('nombre')
        self.apellido = datos.get('apellido')
        self.email = datos.get('email')              # Usamos 'email' como en tu SQL
        self.password = datos.get('password')
        self.fecha_nacimiento = datos.get('fecha_nacimiento')
        self.created_at = datos.get('created_at')
        self.updated_at = datos.get('updated_at')

    @classmethod
    def guardar(cls, datos):
        query = """
        INSERT INTO usuarios (nombre, apellido, email, password, fecha_nacimiento)
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        if not resultados or len(resultados) < 1:
            return False
        return cls(resultados[0])

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        if not resultados or len(resultados) < 1:
            return False
        return cls(resultados[0])

    @staticmethod
    def validar_registro(datos_usuario):
        es_valido = True

        # Nombre: solo validar longitud
        if len(datos_usuario['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        # Apellido: solo validar longitud
        if len(datos_usuario['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        # Email: verificar que no esté vacío y no exista previamente
        if len(datos_usuario['email'].strip()) < 1:
            flash("El correo electrónico no puede estar vacío.", "registro")
            es_valido = False
        else:
            usuario_existente = Usuario.obtener_por_email({'email': datos_usuario['email']})
            if usuario_existente:
                flash("Este correo electrónico ya está registrado.", "registro")
                es_valido = False

        # Contraseña: al menos 8 caracteres
        if len(datos_usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False

        # Confirmación de contraseña
        if datos_usuario['password'] != datos_usuario['confirmar_password']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False

        # Fecha de Nacimiento (Mayoría de edad)
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