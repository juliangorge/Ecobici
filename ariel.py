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
        while cont != 0:
            informacion_archivo.append(datos_linea)
            datos_linea = leer_archivo(archivo,vacio)
        cont += 1
    archivo.close()
    return informacion_archivo


def lectura_estaciones(direccion):
    lista_estaciones = recorrer_archivo("estaciones.csv")
    estaciones = {}
    for datos_estacion in lista_estaciones:
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        bicicletas_ancladas =[]
        cantidad_usos_estacion = []
        estaciones[int(datos_estacion[3])] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4],bicicletas_ancladas,cantidad_usos_estacion]
    return estaciones
    
def lectura_bicicletas(direccion,estaciones):
    lista_bicicletas = recorrer_archivo("bicicletas.csv")
    bicicletas = {}
    #estado,ubicacion
    estado  = "ok"
    ubicacion = "anclada"
    for datos_bicicleta in lista_bicicletas:
        bicicletas[datos_bicicleta[1]] = [estado,ubicacion]
        claves = estaciones.keys()
        numero_estacion = choice(estaciones)
        while (len(estaciones[numero_estacion][4]) >= 30):
            numero_estacion = choice(estaciones.keys)
        estaciones[numero_estacion][4].append(datos_bicicleta[1])
    return bicicletas, estaciones

def lectura_archivos():
    estaciones =  lectura_estaciones('estaciones.csv')
    #bicicletas, estaciones = lectura_bicicletas ('bicicletas.csv',estaciones)
    return estaciones

estaciones =  lectura_archivos()   
print (estaciones)
#print(bicicletas)