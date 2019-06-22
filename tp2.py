from random import randint, random,uniform
import os

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
    lista_estaciones = recorrer_archivo("estaciones.csv")
    estaciones = {}
    bicicletas_ancladas = []
    cantidad_usos_estacion = 0
    for datos_estacion in lista_estaciones:
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        estaciones[int(datos_estacion[3])] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4], bicicletas_ancladas,cantidad_usos_estacion]
    return estaciones

def lectura_bicicletas(estaciones):
    lista_bicicletas = recorrer_archivo("bicicletas.csv")
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
        while (len(estaciones[numero_estacion][4]) >= 29): #sub4 esta la lista de bicicletas ancladas
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
    bicicletas, estaciones = lectura_bicicletas (estaciones)
    print (estaciones)
    print(bicicletas)
    merge_usuarios()
    usuarios = lectura_usuarios()
    return estaciones, bicicletas, usuarios

def listar_usuarios(usuarios):
    #muestra un listado de usuarios
    lista_usuarios = []
    for dni in usuarios:
        lista_usuarios.append([dni, usuarios[dni][0]])
    lista_usuarios.sort(key= lambda usuario: usuario[0])
    print("Usuarios en el sistema: ", len(lista_usuarios))
    for indice in range(0,len(lista_usuarios)):
        print((indice+1), lista_usuarios[indice][0], lista_usuarios[indice][1] )

def alta_usuario(usuarios):
    #Recibe el diccionario de usuarios y añado uno nuevo, luego de validar los datos ingresados por el usuario
    dni = validar_dni ("Ingrese su DNI: ")
    if not dni in usuarios:
        pin = validar_pin ("Ingrese su pin: ")
        nombre = validar_nombre ("Ingrese su nombre y apellido: ")
        celular = validar_celular ("Ingrese su numero de celular: ")
        usuarios[dni] = [nombre,celular,pin, 0, 0] #inicializo en 0 la cantidad de viajes y los minutos de viaje del usuario nuevo
        print("Su usuario ha sido creado.")
        informacion_usuario =  "{},{},{},{}".format(nombre,celular,dni,pin)
        #subir_usuario_al_archivo(informacion_usuario)
        return(usuarios)
    print("Usted ya tiene un usuario")
    return(usuarios)   

def validar_dni (mensaje):
    #Recibe el DNI y verifica si está bien ingresado
    dni = input (mensaje)
    if  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return int(dni)
    return validar_dni("El DNI es incorrecto, ingreselo nuevamente: ")    

def validar_pin (mensaje):
    #Recibe el pin y verifica si está bien ingresado
    pin = input (mensaje)
    if len (pin) == 4 and pin.isdigit() :
        return int(pin)
    return validar_pin("Ingrese un pin correcto: ")

def validar_nombre (mensaje):
    #Recibe el nombre y verifica si está bien ingresado
    nombre = input (mensaje)
    if not nombre.isdigit():
        return (nombre)
    return validar_nombre("Ingrese un nombre y apellido correcto: ")

def validar_celular (mensaje):
    #Recibe el celular y verifica si está bien ingresado
    celular = str(input (mensaje))
    contador_digitos_numericos = 0
    for caracter in celular: 
        if caracter in "123456789()+-0":
            if caracter in "1234567890":
                contador_digitos_numericos +=1
        else: 
            return validar_celular("Ingrese un numero de celular valido: ")
    if contador_digitos_numericos >= 8:
        return celular
    else:
        return validar_celular("Ingrese un numero de celular valido:")

def modificar_pin(usuarios,usuarios_bloqueados):
    #Recibe el dni y modifica su pin
    usuarios, dni = validar_bloqueo(usuarios,usuarios_bloqueados)
    if not dni in usuarios_bloqueados:
        print("Cambiando su PIN")
        pin_nuevo =validar_pin("Ingrese su nuevo pin: ")
        pin_nuevo2 = validar_pin("Reingrese su nuevo pin: ")
        while pin_nuevo != pin_nuevo2:
            print("Los pins no son iguales, ingreselos nuevamente")
            pin_nuevo = validar_pin("Ingrese su pin: ")
            pin_nuevo2 = validar_pin("Reingrese su pin: ")
        usuarios[dni][2] = pin_nuevo
        cambiar_pin_archivo(dni, pin_nuevo)
        print("Su nuevo pin es: ",pin_nuevo)
    else:
        print("Su usuario esta bloqueado, no puede modificar su pin.")
    return (usuarios,usuarios_bloqueados)
def cambiar_pin_archivo(dni,pin_nuevo):
    archivo_usuarios = open('usuarios.csv', 'r', encoding = 'utf-8')
    lineas_usuario = archivo_usuarios.readlines()
    archivo_usuarios.close()
    archivo_usuarios = open('usuarios.csv', 'w', encoding = 'utf-8')
    for linea in lineas_usuario:
        lista_linea = linea.split(",")
        if lista_linea[2] == dni:
            linea= "{},{},{},{}".format(lista_linea[0],lista_linea[1],dni,pin_nuevo)
        archivo_usuarios.write(linea)
    archivo_usuarios.close()

def validar_bloqueo(usuarios,usuarios_bloqueados):
    #ingresa sus datos el usuario, si es necesario lo bloquea (si falla 3 veces el ingreso del pin)  
    dni = validar_dni("Ingrese su DNI: ")
    #print(usuarios)
    while not dni in usuarios:
        print("El dni es incorrecto o usted no tiene un usuario")
        return validar_bloqueo(usuarios,usuarios_bloqueados)
    while not dni in usuarios_bloqueados:
        claves_usuarios = usuarios.keys()
        while not dni in claves_usuarios:
            print("El usuario no existe, ingrese un usuario valido ")
            return validar_bloqueo(usuarios,usuarios_bloqueados)    
        intentos = 2 #Considerando el primer INGRESO como intento nº1
        pin = validar_pin("Ingrese su pin: ")
        while usuarios[dni][2] != pin:
            if(intentos <= 3):
                intentos += 1
                pin = validar_pin("Su pin es incorrecto. Ingreselo nuevamente: ")
            else:   
                bloquear_usuario(dni,usuarios,usuarios_bloqueados)
                return (usuarios,dni)
        return(usuarios,dni)
    
    return(usuarios,dni)

def bloquear_usuario(dni,usuarios,usuarios_bloqueados):
    #Recibe la lista de usuarios bloqueados añade el usuario a bloquear
    usuarios_bloqueados.append(dni)
    usuarios[dni][2] = None
    print('Usuario bloqueado!')
    return (usuarios,usuarios_bloqueados)

def usuarios_menu (usuarios, usuarios_bloqueados):
    print('1 - Listado')
    print('2 - Alta')
    print('3 - Modificación')
    print('4 - Desbloquear')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    
    while opcion not in ['1','2','3','4','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        listar_usuarios(usuarios)
    elif opcion == '2':
        usuarios = alta_usuario(usuarios)
    elif opcion == '3':
        usuarios,usuarios_bloqueados = modificar_pin(usuarios,usuarios_bloqueados)
    elif opcion == '4':
        usuarios,usuarios_bloqueados = desbloquear_usuario(usuarios, usuarios_bloqueados)
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    return (usuarios, usuarios_bloqueados)

def retiros_automaticos_menu (estaciones, bicicletas, usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados):
    print('1 - Viaje aleatorio')
    print('2 - Viajes aleatorios múltiples')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion(1,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '2':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion_con_parametro(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    return (estaciones, bicicletas, usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados)

def informes_menu (estaciones, usuarios, bicicletas_en_reparacion):
    print('1 - Usuarios con mayor cantidad de viajes')
    print('2 - Usuarios con mayor duración acumulada de viajes')
    print('3 - Bicicletas en reparación')
    print('4 - Estaciones más activas')
    print('5 - Reporte de robos')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','4', '5', '0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        informe_cantidad_viajes(usuarios)
    elif opcion == '2':
        informe_duracion_viajes(usuarios)
    elif opcion == '3':
        bicicletas_reparacion(bicicletas_en_reparacion)
    elif opcion == '4':
        top_estaciones(estaciones)
    elif opcion == '0':
        os.system('clear') #Limpia la terminal

def ingreso_al_sistema_menu (estaciones, usuarios, usuarios_bloqueados, bicicletas, bicicletas_en_reparacion, viajes_actuales, viajes_finalizados):
    print('1 - Modificar PIN')
    print('2 - Retirar Bicicleta')
    print('3 - Devolver bicicletas')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        usuarios,usuarios_bloqueados = modificar_pin(usuarios,usuarios_bloqueados)
    elif opcion == '2':
        estaciones,bicicletas, usuarios, viajes_actuales, usuarios_bloqueados = retirar_bicicleta_ingreso(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
    elif opcion == '3':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = validar_ingreso_devolver_bicicleta(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    return (estaciones, usuarios, usuarios_bloqueados, bicicletas, bicicletas_en_reparacion, viajes_actuales, viajes_finalizados)

##############################
######     MAIN CODE    ######
##############################

def menu (estaciones, bicicletas, usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados, bicicletas_en_reparacion):
    seguir = True
    while seguir == True:
        print('¡Bienvenido!\n')
        print('1 - Carga de datos')
        print('2 - Usuarios')
        print('3 - Retiros automáticos')
        print('4 - Informes')
        print('5 - Ingresar al sistema')
        print('0 - Salir \n')
        #Si se ingresa un valor distinto, vuelve al menú raíz
        opcion = input('Elige una opción para continuar: ')
        if opcion == '0':
            seguir = False
        elif opcion == '1':
            estaciones,bicicletas,usuarios = carga_de_datos()
        elif opcion == '2':
           usuarios,usuarios_bloqueados = usuarios_menu(usuarios,usuarios_bloqueados)
        elif opcion == '3':
            estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = retiros_automaticos_menu (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
        elif opcion == '4':
            informes_menu(estaciones,usuarios,bicicletas_en_reparacion)
        elif opcion == '5':
            #Ingreso al sistema
            estaciones,usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados = ingreso_al_sistema_menu(estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados)
        else:
            os.system('clear') #Limpia la terminal
            print('Vuelva a intentarlo')

#Inicializo diccionarios
estaciones = {}
bicicletas = {}
usuarios = {}
usuarios_bloqueados = []
viajes_actuales = {}
viajes_finalizados = {}
bicicletas_en_reparacion = []

### Arranco programa
os.system('clear') ##Limpia la terminal

menu(estaciones, bicicletas, usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados, bicicletas_en_reparacion)

# Funciones:
# Ariel: Treaer archivos (leer y asignar bicicletas a estaciones)
# Franco: dar de alta un usuario (TP1), guardar viajes finalizados en archivo
# Julieta: ingresar al sistema (TP1), guardar viajes en curso en archivo binario
# Julian: retirar y devolver (TP1), 
# Ariel: Simula muchas veces (agregar distancia recorrida en km) -> Haversigne (geopy)

# Informes.
# Adicionales TP2.
# Guardar usuarios creados en archivo maestro usuarios.
# Generar maestro usuarios con los 4 archivos de usuarios (en cara de que existan).
# Viajes en curso se guardan en archivo binario.
# Al comenzar el programa se finalizan los viajes en curso.
# Roban bici e ingresar al sistema.
# Informe de bicicletas robadas y viajes robadas.