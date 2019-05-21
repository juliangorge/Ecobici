def carga_datos_automatica(estaciones, bicicletas, usuarios):
    #Crear 10 estaciones, 5 usuarios, 250 bicis
    #Cargar las bicis en las estaciones "a mano"
    
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    
    #Cargo valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas(estaciones, bicicletas)
    return (estaciones,bicicletas,usuarios)

def carga_datos_random(estaciones, bicicletas, usuarios):
    #Distribuir 250 bicis aleatoriamente en estaciones
    
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    
    #Cargo valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas_random(estaciones, bicicletas)

    return (estaciones,bicicletas,usuarios)

def alta_usuario(usuarios):
    dni = validar_dni ("Ingrese su DNI: ")
    pin = validar_pin ("Ingrese su pin: ")
    nombre = validar_nombre ("Ingrese su nombre y apellido: ")
    celular = validar_celular ("Ingrese su numero de celular: ")
    
    usuarios[dni] = [nombre,celular,pin]


def validar_dni (mensaje):
    dni = input (mensaje)
    while  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return int(dni)
    return validar_dni("El DNI es incorrecto, ingreselo nuevamente: ")    

###########
#### VALIDAR QUE EL DNI EXISTE

def validar_pin (mensaje):
    pin = input (mensaje)
    contador = 0
    while len (pin) == 4 and pin.isdigit() :
        return int(pin)
    return validar_pin("Ingrese un pin correcto: ")


def bloquear_usuario(dni):
    print("aca se bloquea el usuario")
    return 0

def validar_nombre (mensaje):
    nombre = input (mensaje)
    while not nombre.isdigit():
        return (nombre)
    return validar_nombre("Ingrese un nombre y apellido correcto: ")

def validar_celular (mensaje):
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
        return validar_celular("Ingrese un numero de celular valido: ")

def ingresar_usuario (usuarios):
    dni = validar_dni("Ingrese su DNI: ")
    pin = validar_pin("Ingrese su pin: ")
    existencia_usuario =  validar_usuario(dni,pin,usuarios)
    if existencia_usuario == "existe":
        print ("Bienvenido ", usuarios[dni[0]])
        usuarios = modificar_pin(dni,usuarios)
        print(usuarios)
    elif existencia_usuario == "pin incorrecto":
        print("El PIN es incorrecto")
        ingresar_usuario(usuarios)
    elif existencia_usuario == "no existe":
        print("El dni es incorrecto o usted no tiene un usuario")
        ingresar_usuario(usuarios)

        
def validar_usuario(dni,pin,usuarios):
    claves = usuarios.keys()
    if not dni in claves:
        return "no existe"
    else:
        if usuarios[dni][2] == pin:
            return "existe"
        else:
            return "pin incorrecto"
    

def modificar_pin(dni,usuarios):
    print("Cambiando su PIN")
    pin_nuevo =validar_pin("Ingrese su nuevo pin: ")
    pin_nuevo2 = validar_pin("Reingrese su nuevo pin: ")
    while pin_nuevo != pin_nuevo2:
        print("Los pins no son iguales, ingreselos nuevamente")
        pin_nuevo = validar_pin("Ingrese su pin: ")
        pin_nuevo2 = validar_pin("Reingrese su pin: ")
    usuarios[dni][2] = pin_nuevo
    return (usuarios)

def desbloquear_usuario(usuarios, usuarios_bloqueados):
    claves_usuarios = usuarios_bloqueados.keys()
    for i in usuarios_bloqueados:
        print ((i+1), usuarios_bloqueados[i])
    usuario_a_desbloquear = validar_dni('Ingrese el usuario a desbloquear: ')

    if usuario_a_desbloquear in claves_usuarios:
        palabra_secreta = input ("Ingrese la palabra secreta: ")
        if palabra_secreta == 'shimano': 
            print ("Su usuario ha sido desbloqueado.")
            usuarios_bloqueados.remove(usuario_a_desbloquear)
            usuarios[usuario_a_desbloquear][2] = randint(1000,9999)
            print('Su nuevo pin es: ',usuarios[usuario_a_desbloquear][2])
        else: 
            palabra_secreta = input ("La clave ha sido incorrecta. Ingresela nuevamente: ")
    else:
        print ("Su usuario no esta bloqueado.")


#Sólo cuenta las veces que entra a validar: en 3 -> BLOQUEAR
def validar_bloqueo(usuarios):
    dni = validar_dni("Ingrese su DNI: ")
    claves_usuarios = usuarios.keys()
    while not dni in claves_usuarios:
        print("El usuario no existe, ingrese un usuario valido ")
        return validar_bloqueo(usuarios)
    intentos = 0
    pin = validar_pin("Ingrese su pin")
    while usuarios[dni][2] != pin:
        if(intentos <= 3):
            intentos += 1
            pin = validar_pin("Su pin es incorrecto. Ingreselo nuevamente: ")
        else:   
            usuarios = bloquear_usuario(dni)
            return (usuarios)
    return(usuarios)
##verificar si existe estacion

def retirar_bicicleta(estaciones, bicicletas, usuarios):
    #Selecciono número de estación
    

    #Validación ¿y si es vacío o alfanumérico?
    estacion = int(input('Seleccione número de estación: '))
    #Verificar estación
    claves = estaciones.keys()
    while not estacion in claves:
        estacion = int(input('Seleccione número de estación: '))
    #Ingrese su DNI y PIN (3 reintentos sino bloquear usuario)    
    usuarios =  validar_bloqueo(usuarios)        
    numero_anclaje = 0
    while numero_anclaje <= len(estaciones[estacion][3]):
        numero_bicicleta = estaciones[estacion][3][0]
        if(bicicletas[numero_bicicleta][0] == "ok"):
            bicicletas[numero_bicicleta][1] = "En circulación"
            estaciones[estacion][3].remove(numero_bicicleta)
            numero_anclaje = 31 #Salgo de while
            print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje))
            return (estaciones, bicicletas)    
        numero_anclaje += 1     
    print ("No hay bicicleta disponible, intente en otra estacions")            
    return (usuarios,bicicletas,estaciones)        
            
       
def devolver_bicicleta():
    return 0
def simulacion():
    return 0 
def simulacion_con_parametro():
    return 0
def informe():
    #mostrar top de usuarios y estaciones(mirar tp)
    return 0

def cargar_estaciones(estaciones):
    #acumular_lugares_para_anclar = 0
    numero_direccion = 100
    direccion = "Av. Rivadavia {} ".format(numero_direccion)
    latitud = -34.6038
    longitud = -58.3816
    coordenadas = (" {} , {}". format(latitud,(longitud)))
    capacidad = 30
    bicicletas_ancladas = []

    for i in range(1,11):
        if i != 1:
            direccion = "Av. Rivadavia {} ".format(numero_direccion + 100) #suma 100mts a la anterior direccion
            #20 segundos = 100mts
            coordenadas = (" {} / {}". format(latitud,(longitud+0.0020)))
            bicicletas_ancladas = []
        estaciones[i] =  [direccion,coordenadas,capacidad,bicicletas_ancladas]

def cargar_bicicletas(estaciones, bicicletas):
    #si es el primer elemento, id  = 1000 y sino len()+1
    for numero_bicicleta in range(1000,1251):
        if numero_bicicleta < 1240:
            estado = "ok"
        else:
            estado = "reparacion"
        if estado == "reparacion":
            ubicacion = "reparacion"
        else:
            ubicacion = "anclada"
            for i in range(1,11):
                if len(estaciones[i][3]) < 30:
                    estaciones[i][3].append(numero_bicicleta)
        bicicletas[numero_bicicleta] = [estado,ubicacion]

from random import randint, random
def cargar_bicicletas_random(estaciones, bicicletas):
    for numero_bicicleta in range(1000,1251):
        if numero_bicicleta < 1240:
            estado = "ok"
        else:
            estado = "reparacion"
        if estado == "reparacion":
            ubicacion = "reparacion"
        else:
            ubicacion = "anclada"
            numero_estacion = randint(1,10)
            if(len(estaciones[numero_estacion][3]) < 30):
                    estaciones[numero_estacion][3].append(numero_bicicleta)
        bicicletas[numero_bicicleta]= [estado,ubicacion]


def cargar_usuario(usuarios):
    pre_nombres = ['Pablo Guarna','Julieta Ponti','Julián Gorge','Ariel Pisterman','Francopre Cuppari']
    pre_celular = ['03034568','03034569','12345678','87654321','13578642']

    dni = 9999999
    pin = 1000
    for i in range(1,6):
        nombre = pre_nombres[i-1]
        celular = pre_celular[i-1]

        dni += 1
        pin += 10

        usuarios[dni] = [nombre,celular,pin]

def mostrar_bicicletas(bicicletas):
    for bici in bicicletas:
        print (bici, bicicletas[bici])
def listar_usuarios(usuarios):
    claves = usuarios.keys()
    lista_usuarios = []
    for dni in claves:
         lista_usuarios.append([dni, usuarios[dni][0]])
    lista_usuarios.sort(key= lambda usuario: usuario[0])
    print("Usuarios en el sistema: ")
    for indice in range(0,len(lista_usuarios)):
        print((indice+1), lista_usuarios[indice][0], lista_usuarios[indice][1] )


### MAIN
import os

def menu(estaciones, bicicletas, usuarios):
    while True:
        print('1 - Carga de datos')
        print('2 - Usuarios')
        print('3 - Retiros automáticos')
        print('4 - Informes')
        print('5 - Ingresar al sistema')
        print('0 - Salir \n')

        #Si se ingresa un valor distinto, vuelve al menú raíz
        opcion = int(input('Elige una opción para continuar: '))
        
        if opcion == 1:
            print('a - Carga automática')
            print('b - Carga automática aleatoria\n')
            print('0 - Salir \n')

            opcion = input('Elige una opción para continuar: ')
            if opcion == 'a':
                estaciones,bicicletas,usuarios = carga_datos_automatica(estaciones, bicicletas, usuarios)
                os.system('clear') ##Limpia la terminal
                print('Datos cargados!\n')
            elif opcion == 'b':
                estaciones,bicicletas,usuarios = carga_datos_random(estaciones, bicicletas, usuarios)
                os.system('clear') ##Limpia la terminal
                print('Datos aleatorios cargados!\n')
            else:
                os.system('clear') ##Limpia la terminal
                print('La opción no existe.\n')

        elif opcion == 2:
            print('a - Listado')
            print('b - Alta')
            print('c - Modificación')
            print('d - Desbloquear')
            print('0 - Salir \n')

            opcion = input('Elige una opción para continuar: ')
            if opcion == 'a':
                listar_usuarios(usuarios)
            if opcion == 'b':
                alta_usuario(usuarios)
            if opcion == 'c':
                ingresar_usuario(usuarios)
            if opcion == 'd':
                desbloquear_usuario(usuarios, usuarios_bloqueados)
            if opcion == '0':
                desbloquear_usuario(usuarios, usuarios_bloqueados)
            else:
                os.system('clear') ##Limpia la terminal
                print('La opción no existe.\n')

        elif opcion == 3:
            print('a - Viaje aleatorio')
            print('b - Viajes aleatorios múltiples')
            print('0 - Salir \n')

            opcion = input('Elige una opción para continuar: ')
            if opcion == 'a':
                return 0
            if opcion == 'b':
                return 0
            if opcion == '0':
                return 0
            else:
                os.system('clear') ##Limpia la terminal
                print('La opción no existe.\n')

        elif opcion == 4:
            print('a - Usuarios con mayor cantidad de viajes')
            print('b - Usuarios con mayor duración acumulada de viajes')
            print('c - Bicicletas en reparación')
            print('d - Estaciones más activas')
            print('0 - Salir \n')

            opcion = input('Elige una opción para continuar: ')
            if opcion == 'a':
                return 0
            if opcion == 'b':
                return 0
            if opcion == 'c':
                return 0
            if opcion == 'd':
                return 0
            if opcion == '0':
                return 0
            else:
                os.system('clear') ##Limpia la terminal
                print('La opción no existe.\n')

        elif opcion == 5:
            ##Ingreso al sistema
            print('1 - Modificar PIN')
            print('2 - Retirar Bicicleta')
            print('3 - Devolver bicicletas')
            print('0 - Salir \n')
            
            #Validacion vacío o alfanumérico
            sistema = int(input('Elige una opción para continuar: '))
            if sistema == 1:
                return 0
            elif sistema == 2:
                usuarios, estaciones, bicicletas = retirar_bicicleta(estaciones, bicicletas, usuarios)
            elif sistema == 3:
                return 0
            elif sistema == 0:
                return 0
            else:
                os.system('clear') ##Limpia la terminal
                print('La opción no existe.\n')

        elif opcion == 0:
            return False
        else:
            os.system('clear') ##Limpia la terminal
            print('Vuelva a intentarlo')


##############################
#        MAIN CODE           #
##############################

#Inicializo diccionarios
estaciones = {}
bicicletas = {}
usuarios = {}
usuarios_bloqueados = {}

### Inicio
os.system('clear') ##Limpia la terminal
print('¡Bienvenido!\n')
menu(estaciones, bicicletas, usuarios)