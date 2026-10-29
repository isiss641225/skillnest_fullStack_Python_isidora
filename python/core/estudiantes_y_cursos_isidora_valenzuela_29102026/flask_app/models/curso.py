from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante

class Curso:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.estudiantes = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos ORDER BY nombre;"
        resultados = connectToMySQL("esquema_estudiantes_cursos").query_db(query)
        cursos = []
        if resultados:
            for c in resultados:
                cursos.append(cls(c))
        return cursos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)

    @classmethod
    def get_curso_con_estudiantes(cls, curso_id):
        query = """
        SELECT c.id AS curso_id, c.nombre AS curso_nombre, c.created_at AS curso_created_at, c.updated_at AS curso_updated_at,
               e.id AS estudiante_id, e.nombre AS estudiante_nombre, e.apellido AS estudiante_apellido,
               e.edad AS estudiante_edad, e.created_at AS estudiante_created_at, e.updated_at AS estudiante_updated_at
        FROM cursos c
        LEFT JOIN estudiantes e ON c.id = e.curso_id
        WHERE c.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_estudiantes_cursos").query_db(query, {"id": curso_id})
        if not resultados:
            return None

        curso = cls({
            "id": resultados[0]["curso_id"],
            "nombre": resultados[0]["curso_nombre"],
            "created_at": resultados[0]["curso_created_at"],
            "updated_at": resultados[0]["curso_updated_at"]
        })

        for fila in resultados:
            if fila["estudiante_id"] is not None:
                estudiante_data = {
                    "id": fila["estudiante_id"],
                    "nombre": fila["estudiante_nombre"],
                    "apellido": fila["estudiante_apellido"],
                    "edad": fila["estudiante_edad"],
                    "created_at": fila["estudiante_created_at"],
                    "updated_at": fila["estudiante_updated_at"],
                    "curso_id": curso.id
                }
                curso.estudiantes.append(Estudiante(estudiante_data))
        return curso