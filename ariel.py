#import geopy
#from geopy import distance
"""
def calcular_distancia():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    #print(distance.distance(newport_ri, cleveland_oh).kilometres)

#calcular_distancia()
def leer_archivo(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        if lista[2] == 'dni':
            return leer_archivo(archivo, vacio)
        return lista[0], lista[1],int(lista[2]),lista[3]
    else:
        return (vacio)

def merge_usuarios():
    usuarios1 = open('usuarios1.csv','r',encoding = 'utf-8')
    usuarios2 = open('usuarios2.csv','r',encoding = 'utf-8')
    usuarios3 = open('usuarios3.csv','r',encoding = 'utf-8')
    usuarios4 = open('usuarios4.csv','r',encoding = 'utf-8')
    nombre1,celular1,dni1,pin1 = leer_archivo(usuarios1, [0,0,999999999,0])
    nombre2,celular2,dni2,pin2 = leer_archivo(usuarios2,[0,0,999999999,0])
    nombre3,celular3,dni3,pin3 = leer_archivo(usuarios3, [0,0,999999999,0])
    nombre4,celular4,dni4,pin4 = leer_archivo(usuarios4, [0,0,999999999,0])

    maestro_usuarios = open('usuarios.csv','w',encoding = 'utf-8')
    
    
    while dni1 !=999999999 or dni2 !=999999999 or dni3 !=999999999 or dni4 !=999999999:
        menor = min(int(dni1),int(dni2),int(dni3),int(dni4))
        while menor  == dni1 and dni1 !=0:
            linea = "{},{},{},{} \n".format(nombre1,celular1,dni1,pin1)
            maestro_usuarios.write(linea)
            nombre1,celular1,dni1,pin1 = leer_archivo(usuarios1,[0,0,999999999,0])
        while menor  == dni2 and dni2 !=0:
            linea = "{},{},{},{} \n".format(nombre2,celular2,dni2,pin2)
            maestro_usuarios.write(linea)
            nombre2,celular2,dni2,pin2 = leer_archivo(usuarios2,[0,0,999999999,0])
        while menor  == dni3 and dni3 !=0:
            linea = "{},{},{},{} \n".format(nombre3,celular3,dni3,pin3)
            maestro_usuarios.write(linea)
            nombre3,celular3,dni3,pin3= leer_archivo(usuarios3,[0,0,999999999,0])
        while menor  == dni4 and dni4 !=0:
            linea = "{},{},{},{} \n".format(nombre4,celular4,dni4,pin4)
            maestro_usuarios.write(linea)
            nombre4,celular4,dni4,pin4 = leer_archivo(usuarios4,[0,0,999999999,0])
        
    usuarios1.close()
    usuarios2.close()
    usuarios3.close()
    usuarios4.close()
    maestro_usuarios.close()
    

merge_usuarios()

"""

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
    lista_estaciones = recorrer_archivo("Ecobici/bicicletas.csv")
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
        estaciones[numero_estacion][4].append(datos_bicicleta[1])
    return bicicletas, estaciones

def lectura_bicicletas2(estaciones):
    lista_bicicletas = recorrer_archivo("Ecobici/bicicletas.csv")
    bicicletas = {}
    #estado,ubicacion
    estado  = "ok"
    ubicacion = "anclada"
    numeros_estaciones =[]
    for estacion in estaciones:
        numeros_estaciones.append(int(estacion))
    longitud_numeros_estaciones = len(numeros_estaciones) - 1
    for datos_bicicleta in lista_bicicletas:
        numero_bicicleta = int(datos_bicicleta[1])
        bicicletas[numero_bicicleta] = [estado,ubicacion]
        posicion_estacion = randint(0,longitud_numeros_estaciones)
        numero_estacion = numeros_estaciones[posicion_estacion]
        if (len(estaciones[numero_estacion][4]) >= 29): #sub4 esta la lista de bicicletas ancladas
            posicion_estacion = randint(0,longitud_numeros_estaciones)
            numero_estacion = numeros_estaciones[posicion_estacion]
        estaciones[numero_estacion][4].append(numero_bicicleta)
    return bicicletas, estaciones    


def leer_archivo_usuarios(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        if lista[2] == 'dni':
            return leer_archivo(archivo, vacio)
        return lista[0], lista[1],int(lista[2]),lista[3]
    else:
        return (vacio)

def merge_usuarios():
    usuarios1 = open('usuarios1.csv','r',encoding = 'utf-8')
    usuarios2 = open('usuarios2.csv','r',encoding = 'utf-8')
    usuarios3 = open('usuarios3.csv','r',encoding = 'utf-8')
    usuarios4 = open('usuarios4.csv','r',encoding = 'utf-8')
    nombre1,celular1,dni1,pin1 = leer_archivo_usuarios(usuarios1, [0,0,999999999,0])
    nombre2,celular2,dni2,pin2 = leer_archivo_usuarios(usuarios2,[0,0,999999999,0])
    nombre3,celular3,dni3,pin3 = leer_archivo_usuarios(usuarios3, [0,0,999999999,0])
    nombre4,celular4,dni4,pin4 = leer_archivo_usuarios(usuarios4, [0,0,999999999,0])

    maestro_usuarios = open('maestro_usuarios.csv','w',encoding = 'utf-8')
    while dni1 !=999999999 or dni2 !=999999999 or dni3 !=999999999 or dni4 !=999999999:
        menor = min(int(dni1),int(dni2),int(dni3),int(dni4))
        while menor  == dni1 and dni1 !=0:
            linea = "{},{},{},{} \n".format(nombre1,celular1,dni1,pin1)
            maestro_usuarios.write(linea)
            nombre1,celular1,dni1,pin1 = leer_archivo(usuarios1,[0,0,999999999,0])
        while menor  == dni2 and dni2 !=0:
            linea = "{},{},{},{} \n".format(nombre2,celular2,dni2,pin2)
            maestro_usuarios.write(linea)
            nombre2,celular2,dni2,pin2 = leer_archivo(usuarios2,[0,0,999999999,0])
        while menor  == dni3 and dni3 !=0:
            linea = "{},{},{},{} \n".format(nombre3,celular3,dni3,pin3)
            maestro_usuarios.write(linea)
            nombre3,celular3,dni3,pin3= leer_archivo(usuarios3,[0,0,999999999,0])
        while menor  == dni4 and dni4 !=0:
            linea = "{},{},{},{} \n".format(nombre4,celular4,dni4,pin4)
            maestro_usuarios.write(linea)
            nombre4,celular4,dni4,pin4 = leer_archivo(usuarios4,[0,0,999999999,0])
    usuarios1.close()
    usuarios2.close()
    usuarios3.close()
    usuarios4.close()
    maestro_usuarios.close()

def lectura_usuarios():
    lista_usuarios = recorrer_archivo("maestro_usuarios.csv")
    usuarios = {}
    tiempo_de_viaje = 0
    cantidad_viajes = 0
    for datos_usuario in lista_usuarios:
        #usuarios[dni] = [nombre,celular,pin,tiempo_de_viaje,cantidad_viajes]
        usuarios[datos_usuario[2]] = [datos_usuario[0],datos_usuario[1],datos_usuario[3], tiempo_de_viaje,cantidad_viajes]
    return usuarios
def carga_de_datos():
    estaciones =  lectura_estaciones()
    #print(estaciones)
    bicicletas, estaciones = lectura_bicicletas(estaciones)
    
    #merge_usuarios()
    #usuarios = lectura_usuarios()
    return estaciones, bicicletas


estaciones,bicicletas =carga_de_datos()
print (estaciones)
print(bicicletas)