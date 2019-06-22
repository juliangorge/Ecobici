from random import randint, random,uniform
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

def lectura_estaciones():
    lista_estaciones = recorrer_archivo("Ecobici/estaciones.csv")
    estaciones = {}
    bicicletas_ancladas = []
    cantidad_usos_estacion = 0
    for datos_estacion in lista_estaciones:
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        estaciones[int(datos_estacion[3])] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4], bicicletas_ancladas,cantidad_usos_estacion]
    return estaciones

def lectura_bicicletas(estaciones):
    lista_bicicletas = recorrer_archivo('Ecobici/bicicletas.csv')
    #estado,ubicacion
    estado  = "ok"
    ubicacion = "anclada"
    numeros_estaciones =[]
    bicicletas = {}
    for estacion in estaciones:
        numeros_estaciones.append(estacion)
    
    for datos_bicicleta in lista_bicicletas:
        bicicletas[datos_bicicleta[1]] = [estado,ubicacion]
        
        posicion_estacion = randint(0, (len(numeros_estaciones)-1))
        numero_estacion = numeros_estaciones[posicion_estacion]

        while (len(estaciones[numero_estacion][4]) >= 30):
            posicion_estacion = randint(0, (len(numeros_estaciones)-1))
            numero_estacion = numeros_estaciones[posicion_estacion]
        
        #print('bici #',datos_bicicleta[1],'--> estacion #',numero_estacion)
        estaciones[numero_estacion][4].append(datos_bicicleta[1])
        #print(datos_bicicleta[1])
        #print(numero_estacion,':',estaciones[numero_estacion][4])
        
    #print(estaciones)
    return bicicletas, estaciones

def carga_de_datos():
    estaciones =  lectura_estaciones()
    
    bicicletas, estaciones = lectura_bicicletas(estaciones)
    
    #print(estaciones)
    #merge_usuarios()
    #usuarios = lectura_usuarios()
    return estaciones, bicicletas


estaciones, bicicletas = carga_de_datos()
#print (estaciones)
#print(bicicletas)