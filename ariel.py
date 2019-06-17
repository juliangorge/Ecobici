import geopy
from geopy import distance

def calcular_distancia():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    print(distance.distance(newport_ri, cleveland_oh).kilometres)




from random import randint, uniform, choice
def leer_archivo(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        return (lista)
    else:
        return (vacio)

def recorrer_archivo(direccion):
    archivo = open(direccion,'r', encoding='utf-8')
    vacio = []
    informacion_archivo = []
    datos_linea = leer_archivo(archivo,vacio)
    cont = 0
    while datos_linea:
        if cont != 0:
            informacion_archivo.append(datos_linea)
        cont += 1
        datos_linea = leer_archivo(archivo,vacio)    
    archivo.close()
    return informacion_archivo


def lectura_estaciones(direccion):
    lista_estaciones = recorrer_archivo("estaciones.csv")
    estaciones = {}
    for datos_estacion in lista_estaciones:
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        bicicletas_ancladas = []
        cantidad_usos_estacion = 0
        estaciones[int(datos_estacion[3])] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4], bicicletas_ancladas,cantidad_usos_estacion]
    return estaciones
    
def lectura_bicicletas(direccion,estaciones):
    lista_bicicletas = recorrer_archivo("bicicletas.csv")
    bicicletas = {}
    #estado,ubicacion
    estado  = "ok"
    ubicacion = "anclada"
    numeros_estaciones =[]
    for estacion in estaciones:
        numeros_estaciones.append(estacion)
    for datos_bicicleta in lista_bicicletas:
        bicicletas[datos_bicicleta[1]] = [estado,ubicacion]
        posicion_estacion = randint(0,len(numeros_estaciones)-1)
        numero_estacion = numeros_estaciones[posicion_estacion]
        while (len(estaciones[numero_estacion][4]) >= 30):
            numero_estacion = randint(0,len(numeros_estaciones))
        estaciones[numero_estacion][4].append(datos_bicicleta[1])
    return bicicletas, estaciones

def lectura_archivos():
    estaciones =  lectura_estaciones('estaciones.csv')
    bicicletas, estaciones = lectura_bicicletas ('bicicletas.csv',estaciones)
    return estaciones, bicicletas

#estaciones, bicicletas =  lectura_archivos()   
"""
for estacion in estaciones:
    print (len(estaciones[estacion][4]))
    print (estaciones[estacion][3])
#print(bicicletas)
"""
calcular_distancia()