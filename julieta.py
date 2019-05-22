
#b. Top 5 de usuarios de bicicleta, por duración acumulada de los viaje
def top_cinco_duracion (usuarios):
    usuarios_top_cinco = []
    claves_usuarios = usuarios.keys()
#usuarios[dni][3] --> duracion de los viajes del usuario
    for usuario in claves_usuarios:
        usuarios_top_cinco.append ([usuario, usuario[3]])
    usuarios_top_cinco.sort (key = lambda usuario:usuario[1], reverse = True)
    for i in range (0,5):
        print ((i+1), "-", usuarios_top_cinco [0])
#d. Top de estaciones más activas: se entiende por “actividad” a la extracción y la devolución de bicicletas
    #
    # estaciones[i] =  [direccion,coordenadas,capacidad,bicicletas_ancladas,cantidad_de_usos]
def estaciones_mas_activas (estaciones):
    top_estaciones_activas = []
    claves_estaciones = estaciones.keys()
    for estacion in claves_estaciones:
        top_estaciones_activas.append ([estacion, estacion[4]])
    top_estaciones_activas.sort (key = lambda estacion:estacion[1], reverse = True)
    for i in range (0,11):
        print ((i+1), "-", top_estaciones_activas [0])