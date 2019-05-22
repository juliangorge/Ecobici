"""
8) Generar una función que
a. Seleccione un usuario que no esté actualmente en viaje ni bloqueado y una estación al azar
b. Intente retirar una bicicleta para el usuario
c. Genere una duración aleatoria de viaje del usuario menor a 90 minutos
d. Devuelva la bicicleta en otra estación (no la misma)
e. Vaya informando de estas acciones por pantalla, por ejemplo:
i. Juan Pérez retiró la bicicleta 1022 de la estación 3 de Las Heras 3255 a las 12:35:25 h.
ii. Juan Pérez devolvió la bicicleta 1022 en la estación 15 de Gallo 224 a las 13:30:12 h. Al
exceder los 60 minutos de uso ha sido bloqueado.
"""

"""
from random import randint, random
def simulacion(estaciones, bicicletas, usuarios):
    
    estacion_random = randint(1,len(estaciones))

   estacion_random, numero_bicicleta= simular_retiro_bici(estaciones,bicicletas, estacion_random)
    
        

def simular_retiro_bici(estacion_random):
    numero_anclaje = 0
    while numero_anclaje <= len(estaciones[estacion_random][3]):
        numero_bicicleta = estaciones[estacion][3][0]
        if(bicicletas[numero_bicicleta][0] == "ok"):
            bicicletas[numero_bicicleta][1] = "En circulación"
            estaciones[estacion_random][3].remove(numero_bicicleta)
            numero_anclaje = 31 #Salgo de while
            #print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje))
            return (estacion_random, numero_bicicleta)    
        numero_anclaje += 1     
    print ("No hay bicicleta disponible, intente en otra estacions")   

"""
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
    estaciones[i] =  [direccion,coordenadas,capacidad,bicicletas_ancladas,cantidad_de_usos]
def estaciones_mas_activas (estaciones):
    top_estaciones_activas = []
    claves_estaciones = estaciones.keys()
    for estacion in claves_estaciones:
        top_estaciones_activas.append ([estacion, estacion[4]])
    top_estaciones_activas.sort (key = lambda estacion:estacion[1], reverse = True)
    for i in range (0,11):
        print ((i+1), "-", top_estaciones_activas [0])