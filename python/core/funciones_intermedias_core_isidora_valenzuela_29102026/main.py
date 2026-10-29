# ==========================================
# PARTE 1: ACTUALIZACIÓN DE DATOS
# ==========================================

# Estructuras de datos iniciales
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]

streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}

ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

# 1. Cambiar en puntajes el valor 300 por 600
puntajes[1][0] = 600

# 2. Cambiar el nombre de "GameNinjaPro" a "EliteGamerX"
streamers[0]["nombre"] = "EliteGamerX"

# 3. Cambiar en eventos la ciudad "Las Vegas" por "San Francisco"
eventos["Estados Unidos"][2] = "San Francisco"

# 4. Cambiar la latitud de ubicacion a 40.712776
ubicacion[0]["latitud"] = 40.712776


# ==========================================
# PARTE 2: FUNCIONES PARA RECORRER DATOS
# ==========================================

def iterar_diccionario(lista):
    """
    Recorre una lista de diccionarios e imprime cada clave y valor 
    en una sola línea.
    """
    for elemento in lista:
        linea = []
        for clave, valor in elemento.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))

def obtener_valores(clave, lista):
    """
    Imprime el valor asociado a una clave específica para cada diccionario de la lista.
    """
    for elemento in lista:
        if clave in elemento:
            print(elemento[clave])


# ==========================================
# PARTE 3: MOSTRAR INFORMACIÓN DE DICCIONARIO CON LISTAS
# ==========================================

def mostrar_informacion(diccionario):
    """
    Imprime la cantidad de elementos y la clave en mayúsculas, 
    seguido de cada elemento de la lista en líneas separadas.
    """
    for clave, lista in diccionario.items():
        print(f"\n{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)


# ==========================================
# PRUEBAS Y VERIFICACIÓN
# ==========================================

print("--- Prueba: iterar_diccionario ---")
iterar_diccionario(streamers)

print("\n--- Prueba: obtener_valores ('nombre') ---")
obtener_valores("nombre", streamers)

print("\n--- Prueba: obtener_valores ('seguidores') ---")
obtener_valores("seguidores", streamers)

print("\n--- Prueba: mostrar_informacion ---")
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

mostrar_informacion(categorias)