# 1.- Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
cambio = puntajes[1][0] = 600
print(puntajes)

# 2.- Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"
print(streamers)

# 3.- Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
} 
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)


# 4.- Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"] = 40.712776
print(ubicacion)

# 5.- Formatea la salida para que cada diccionario se imprima en una sola línea
def iterar_diccionario(lista):
   for streamer in streamers:
      print(f"nombre - {streamer["nombre"]}, seguidores - {streamer["seguidores"]}")
iterar_diccionario(streamers)

# 6.- Funciones para recorrer y representar datos
def obtener_valores(clave, lista):
   for i in range(len(lista)):
      if lista[i] in lista:
         print(lista[i][clave]) 
obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)

# 7.- Mostrar información de un diccionario con listas
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

def mostrar_informacion(diccionario):
   for categoria, items in diccionario.items():
       print(f"{len(items)} {categoria.upper()}")
       for item in items:
           print(item)
mostrar_informacion(categorias)
