# ==========================================================
# MODELO MASCOTA
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Convierte un diccionario de MySQL en un objeto Mascota.
        """
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Devuelve todas las mascotas de la base de datos.
        """
        query = """
            SELECT *
            FROM mascotas;
        """

        resultados = connectToMySQL("primera_flask").query_db(query)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas


    # ======================================================
    # OBTENER MASCOTAS POR TIPO (Para /mascotas/perros)
    # ======================================================

    @classmethod
    def get_by_type(cls, tipo):
        """
        Consulta las mascotas filtradas por el atributo 'tipo'.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo)s;
        """

        data = {
            "tipo": tipo
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas


    # ======================================================
    # OBTENER MASCOTA POR ID (Para /mascota/<int:id>)
    # ======================================================

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota utilizando su ID.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """

        data = {
            "id_mascota": id
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None