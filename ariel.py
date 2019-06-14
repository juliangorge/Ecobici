from random import randint, random,uniform

def leer_archivo(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        return (lista)
    else:
        return (vacio)

def lectura_estaciones(direccion):
    estaciones = {}
    archivo = open(direccion,'r', encoding='utf-8')
    vacio = []
    datos_estacion = leer_archivo(archivo,vacio)
    while datos_estacion:
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        bicicletas_ancladas =[]
        cantidad_usos_estacion = []
        estaciones[datos_estacion[3]] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4],bicicletas_ancladas,cantidad_usos_estacion]
        datos_estacion = leer_archivo(archivo,vacio)
    archivo.close()
    return estaciones
    
def lectura_bicicletas(direccion,estaciones):
    bicicletas = {}
    archivo = open(direccion,'r', encoding='utf-8')
    vacio = []
    datos_bicicleta = leer_archivo(archivo,vacio)
    while datos_bicicleta:
        #estado,ubicacion
        estado  = "ok"
        ubicacion = "anclada"
        bicicletas[datos_bicicleta[1]] = [estado,ubicacion]
        numero_estacion = randint(1,300)
        claves_estacion = estaciones.keys()
        while not numero_estacion in claves_estacion:
            numero_estacion = randint(1,300)
        if(len(estaciones[numero_estacion][3]) < 30):
            estaciones[numero_estacion][4].append(datos_bicicleta[1])
        datos_bicicleta = leer_archivo(archivo,vacio)
    archivo.close()
    return bicicletas, estaciones

def lectura_archivos():
    estaciones =  lectura_estaciones('estaciones.csv')
    bicicletas, estaciones = lectura_bicicletas ('bicicletas.csv',estaciones)
    return estaciones, bicicletas

estaciones,bicicletas =  lectura_archivos()   
print (estaciones)
print(bicicletas)