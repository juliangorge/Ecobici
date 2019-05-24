from random import randint, random,uniform
import os
def carga_datos_automatica(estaciones, bicicletas, usuarios):
    #Crea 10 estaciones, 5 usuarios, 250 bicis
    #Carga las bicis en las estaciones "a mano"
    
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    #Cargo valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas(estaciones, bicicletas)
    print("Datos cargados!")
    return (estaciones,bicicletas,usuarios)

def carga_datos_random(estaciones, bicicletas, usuarios):
    #Crea 10 estaciones, 5 usuarios, 250 bicis
    #Distribuye y crea 250 bicis aleatoriamente en estaciones
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    #Carga valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas_random(estaciones, bicicletas)
    print("Datos cargados aleatoriamente!")
    return (estaciones,bicicletas,usuarios)

def cargar_estaciones(estaciones):
    #acumular_lugares_para_anclar = 0
    numero_direccion = 100
    direccion = "Av. Rivadavia {} ".format(numero_direccion)
    latitud = -34.6038
    longitud = -58.3816
    coordenadas = (" {} , {}". format(latitud,(longitud)))
    capacidad = 30
    bicicletas_ancladas = []
    cantidad_usos_estacion = 0
    for i in range(1,11):
        if i != 1:
            numero_direccion+= 100
            direccion = "Av. Rivadavia {} ".format(numero_direccion ) #suma 100mts a la anterior direccion
            #20 segundos = 100mts
            coordenadas = (" {} / {}". format(latitud,(longitud+0.0020)))
            bicicletas_ancladas = []
        estaciones[i] = [direccion,coordenadas,capacidad,bicicletas_ancladas,cantidad_usos_estacion]

def cargar_bicicletas(estaciones, bicicletas):
    #carga las bicicletas al sistema 
    #si es el primer elemento, id  = 1000 y sino len()+1
    numero_estaciones = 1
    for numero_bicicleta in range(1000,1251):
        if numero_bicicleta < 1241:
            estado = "ok"
        else:
            estado = "reparacion"
        if estado == "reparacion":
            ubicacion = "reparacion"
            bicicletas_en_reparacion.append(numero_bicicleta)
        else:
            ubicacion = "anclada"
            if len(estaciones[numero_estaciones][3]) < 25:
                estaciones[numero_estaciones][3].append(numero_bicicleta)
            else:
                numero_estaciones += 1
                estaciones[numero_estaciones][3].append(numero_bicicleta)
                #print(estaciones[numero_estaciones])
            bicicletas[numero_bicicleta] = [estado, ubicacion]

def cargar_bicicletas_random(estaciones, bicicletas):
    #carga las bicicletas al sistema de forma aleatoria dentro de las estaciones
    for numero_bicicleta in range(1000,1251):
        if numero_bicicleta < 1241:
            estado = "ok"
        else:
            estado = "reparacion"
        if estado == "reparacion":
            ubicacion = "reparacion"
            bicicletas_en_reparacion.append(numero_bicicleta)
        else:
            ubicacion = "anclada"
            numero_estacion = randint(1,10)
            if(len(estaciones[numero_estacion][3]) < 30):
                    estaciones[numero_estacion][3].append(numero_bicicleta)
        bicicletas[numero_bicicleta]= [estado,ubicacion]

def cargar_usuario(usuarios):
    #carga los usuarios al sistema
    pre_nombres = ['Uriel Kelman','Julieta Ponti','Julián Gorge','Ariel Pisterman','Franco Cuppari']
    pre_celular = ['03034568','03034569','12345678','87654321','13578642']
    tiempo_de_viaje = 0
    dni = 9999999
    pin = 1000
    cantidad_viajes = 0
    for i in range(1,6):
        nombre = pre_nombres[i-1]
        celular = pre_celular[i-1]
        dni += 1
        pin += 10
        usuarios[dni] = [nombre,celular,pin,tiempo_de_viaje,cantidad_viajes]

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
    while not dni in usuarios:
        pin = validar_pin ("Ingrese su pin: ")
        nombre = validar_nombre ("Ingrese su nombre y apellido: ")
        celular = validar_celular ("Ingrese su numero de celular: ")
        usuarios[dni] = [nombre,celular,pin, 0, 0] #inicializo en 0 la cantidad de viajes y los minutos de viaje del usuario nuevo
        print("Su usuario ha sido creado.")
        return(usuarios)
    print("Usted ya tiene un usuario")
    return(usuarios)   

def validar_dni (mensaje):
    #Recibe el DNI y verifica si está bien ingresado
    dni = input (mensaje)
    while  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return int(dni)
    return validar_dni("El DNI es incorrecto, ingreselo nuevamente: ")    

def validar_pin (mensaje):
    #Recibe el pin y verifica si está bien ingresado
    pin = input (mensaje)
    while len (pin) == 4 and pin.isdigit() :
        return int(pin)
    return validar_pin("Ingrese un pin correcto: ")

def validar_nombre (mensaje):
    #Recibe el nombre y verifica si está bien ingresado
    nombre = input (mensaje)
    while not nombre.isdigit():
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
 
"""      
def ingresar_usuario_modificacion(usuarios):
    #Recibe el diccionario usuario y verifica si los datos ingresados corresponden a un usuario existente,
    # y le permite modificar su pin.
    dni = validar_dni("Ingrese su DNI: ")
    pin = validar_pin("Ingrese su pin: ")
    existencia_usuario =  validar_usuario(dni,pin,usuarios)
    
    while existencia_usuario == "no existe":
        print("El dni es incorrecto o usted no tiene un usuario")
        return ingresar_usuario_modificacion(usuarios)
    while existencia_usuario == "pin incorrecto":
        print("El PIN es incorrecto")
        pin = validar_pin("Ingrese su pin: ")
        existencia_usuario = validar_usuario(dni,pin,usuarios)
    while existencia_usuario == "existe":
        print ("Bienvenido ", usuarios[dni][0])
        usuarios = modificar_pin(dni,usuarios)
        return(usuarios) 
     
def validar_usuario(dni,pin,usuarios):
    #Recibe el diccionario usuarios 
    #Verifica si los datos ingresados corresponden a un usuario existente.
    #verifica si el pin es igual al ingresado
    if not dni in usuarios:
        return "no existe"
    else:
        if usuarios[dni][2] == pin:
            return "existe"
        else:
            return "pin incorrecto"
"""    
def modificar_pin(usuarios,usuarios_bloqueados):
    #Recibe el dni y modifica su pin
    usuarios, dni = validar_bloqueo(usuarios,usuarios_bloqueados)
    while not dni in usuarios_bloqueados:
        print("Cambiando su PIN")
        pin_nuevo =validar_pin("Ingrese su nuevo pin: ")
        pin_nuevo2 = validar_pin("Reingrese su nuevo pin: ")
        while pin_nuevo != pin_nuevo2:
            print("Los pins no son iguales, ingreselos nuevamente")
            pin_nuevo = validar_pin("Ingrese su pin: ")
            pin_nuevo2 = validar_pin("Reingrese su pin: ")
        usuarios[dni][2] = pin_nuevo
        print("Su nuevo pin es: ",pin_nuevo)
        return (usuarios,usuarios_bloqueados)
    print("Su usuario esta bloqueado, no puede modificar su pin.")
    return (usuarios,usuarios_bloqueados)
    
def bloquear_usuario(dni,usuarios,usuarios_bloqueados):
    #Recibe la lista de usuarios bloqueados añade el usuario a bloquear
    usuarios_bloqueados.append(dni)
    usuarios[dni][2] = None
    print('Usuario bloqueado!')
    return (usuarios,usuarios_bloqueados)

def desbloquear_usuario(usuarios, usuarios_bloqueados):
    #Lista a los usuarios bloqueados y permite desbloquear el usuario
    for usuario in usuarios_bloqueados:
        print (usuario, usuarios[usuario][0])
    usuario_a_desbloquear = validar_dni('Ingrese el dni del usuario a desbloquear: ')
    if usuario_a_desbloquear in usuarios_bloqueados:
        palabra_secreta = input ("Ingrese la palabra secreta: ")
        while not palabra_secreta == 'shimano':    
            palabra_secreta = input ("La clave ha sido incorrecta. Ingresela nuevamente: ")
        print ("Su usuario ha sido desbloqueado.")
        usuarios_bloqueados.remove(usuario_a_desbloquear)
        usuarios[usuario_a_desbloquear][2] = randint(1000,9999) #asigno nuevo pin
        print('Su nuevo pin es: ',usuarios[usuario_a_desbloquear][2])
        return usuarios, usuarios_bloqueados    
    else:
        print ("Su usuario no está bloqueado.")
        return usuarios, usuarios_bloqueados

def seleccionar_usuario(usuarios, viajes_actuales,usuarios_bloqueados):
    #Elige usuario a simular, si no hay usuarios disponibles devuelve -1
    usuario_a_viajar = -1
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][2]])
    indice_usuario = 0
    if (len(usuarios) == 0):
        print("No hay usuarios")
        return usuario_a_viajar
    else: 
        listado_pins = []
        while usuario_a_viajar == -1:
            indice_usuario = randint(0,(len(lista_usuarios)-1))
            if lista_usuarios[indice_usuario][0] not in usuarios_bloqueados and lista_usuarios[indice_usuario][0] not in viajes_actuales:
                #asigna el usuario
                usuario_a_viajar = usuario_a_viajar =  lista_usuarios[indice_usuario][0]
            else:
                #hago una lista con los usuarios bloqueados para compararla con usuarios y ver cuando no hay mas usuarios disponibles
                if indice_usuario not in listado_pins:
                    listado_pins.append(indice_usuario)
                if len(listado_pins) == len (lista_usuarios):
                    #print(listado_pins)
                    return(usuario_a_viajar)
        return (usuario_a_viajar)
#ACA VAN LAS DOS SIMULACIONES

def informe_cantidad_viajes(usuarios):
    #muestra los 10 usuarios que mas viajes hicieron
    lista_usuarios = []
    #usuarios[dni][4] --> cantidad viajes usuario
    for usuario in usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][0], usuarios[usuario][4]])
    lista_usuarios.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,len(lista_usuarios)):
        if(i <= 10):
            print ((i+1), "-", lista_usuarios[i][1], '(' , lista_usuarios[i][0] , ') con' , lista_usuarios[i][2], "viajes\n")

def informe_duracion_viajes (usuarios):
    #muestra los 5 usuarios con mas duracion acumulada de viajes
    lista_usuarios = []
    claves_usuarios = usuarios.keys()
    #usuarios[dni][3] --> duracion de los viajes del usuario
    for usuario in claves_usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][0], usuarios[usuario][3]])
    lista_usuarios.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,5):
        print ((i+1), "-", lista_usuarios[i][1], '(' , lista_usuarios[i][0], ') con' , lista_usuarios[i][2], "minutos\n")

def bicicletas_reparacion(bicicletas_en_reparacion):
    #muestra las bicicletas en reparacion
    print('Bicicletas en reparación: {}\n'.format(len(bicicletas_en_reparacion)))
    for bicicleta in bicicletas_en_reparacion:
        print(bicicleta)

def top_estaciones (estaciones):
    #muestra las estaciones mas activas
    top_estaciones_activas = []
    for estacion in estaciones:
        top_estaciones_activas.append([estacion, estaciones[estacion][4]])
    top_estaciones_activas.sort (key = lambda estacion:estacion[1], reverse = True)
    for i in range (0,10):
        print ((i+1) , "- Estacion: #" , top_estaciones_activas[i][0], 'con', top_estaciones_activas[i][1], 'usos')

def validar_bloqueo(usuarios,usuarios_bloqueados):
    #ingresa sus datos el usuario, si es necesario lo bloquea (si falla 3 veces el ingreso del pin)  
    dni = validar_dni("Ingrese su DNI: ")
    print(usuarios)
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
    print("Su usuario esta bloqueado. No puede retirar una bicicleta")
    return(usuarios,dni)

#aca va retirar y devolver bicicleta
def retirar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
    #Retira una bicicleta del diccionario estaciones y la pone en circulacion (viajes actuales), verificando que el usuario no esté bloqueado
    usuarios,dni = validar_bloqueo(usuarios,usuarios_bloqueados)
    if dni in viajes_actuales:
        print('Usted ya tiene una bicicleta!')
    else:
        if(dni not in usuarios_bloqueados):
            numero_bicicleta,estacion,numero_anclaje = elegir_bicicleta_de_estacion(estaciones,bicicletas)
            while numero_bicicleta != -1:
                bicicletas[numero_bicicleta][1] = "En circulación"
                estaciones[estacion][3].remove(numero_bicicleta)
                print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje+1))
                horario_salida = generar_horario_salida()
                viajes_actuales[dni] = [numero_bicicleta, estacion, horario_salida]
                estaciones[estacion][4] += 1
                return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
            print ("No hay bicicletas disponibles, intente en otra estación")
    return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)

def elegir_bicicleta_de_estacion(estaciones,bicicletas):
    estacion = input('Seleccione número de estación: ')
    claves = estaciones.keys()
    while not int(estacion) in claves or not estacion.isdigit():
        estacion = input('Seleccione un número de estación correcto: ')
    estacion = int(estacion)
    numero_anclaje = 0
    while len(estaciones[estacion][3]) >= numero_anclaje:
        if(len(estaciones[estacion][3]) > 0):
            numero_bicicleta = estaciones[estacion][3][numero_anclaje]
            if(bicicletas[numero_bicicleta][0] == "ok"):
                return numero_bicicleta,estacion,numero_anclaje
        else:
            print ("No hay bicicletas, intente en otra estación")
        numero_anclaje += 1
    numero_bicicleta = -1
    return numero_bicicleta, estacion,numero_anclaje
def generar_horario_salida():
    hora = randint(0,22)
    if(hora == 22):
        minuto = randint(0,30) 
    else:
        minuto = randint(0,59)
    if minuto <10: #agrega el 0 a los minutos si son menores a 10
        horario_salida = str(hora) + ': 0' + str(minuto)
    else:
        horario_salida = str(hora) + ':' + str(minuto)
    return(horario_salida)
def validar_ingreso_devolver_bicicleta(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    dni = validar_dni("Ingrese su numero de dni: ")
    while not dni in usuarios:
        dni = validar_dni("DNI incorrecto. Vuelva a ingresarlo: " )
    if(len(viajes_actuales) and len(viajes_actuales[dni]) > 0):
        estacion = int(input('Seleccione número de estación: '))
        #Verificar estación
        while not estacion in estaciones:
            estacion = int(input('Seleccione número de estación: '))
            devolver_bicicleta(dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    else:    
        print('No tienes ninguna bicicleta para devolver!')
    return estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados


def carga_de_datos_menu(estaciones,bicicletas,usuarios):
    print('1 - Carga automática')
    print('2 - Carga automática aleatoria\n')
    print('0 - Salir \n')
    opcion = input('Elige una opción para continuar: ')
            
    while opcion not in ['1','2','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        estaciones,bicicletas,usuarios = carga_datos_automatica(estaciones, bicicletas, usuarios)
        os.system('clear') ##Limpia la terminal 
        print('Datos cargados!\n')
    elif opcion == '2':
        estaciones,bicicletas,usuarios = carga_datos_random(estaciones, bicicletas, usuarios)   
        os.system('clear') ##Limpia la terminal
        print('Datos aleatorios cargados!\n')
    elif opcion == '0':
        os.system('clear') ##Limpia la terminal
    return (estaciones,bicicletas,usuarios)    

def usuarios_menu (usuarios,usuarios_bloqueados):
    print('1 - Listado')
    print('2 - Alta')
    print('3 - Modificación')
    print('4 - Desbloquear')
    print('0 - Salir \n')
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
        usuarios,usuarios_bloqueados =desbloquear_usuario(usuarios, usuarios_bloqueados)
    elif opcion == '0':
        os.system('clear') ##Limpia la terminal
    return (usuarios,usuarios_bloqueados)

def retiros_automaticos_menu (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    print('1 - Viaje aleatorio')
    print('2 - Viajes aleatorios múltiples')
    print('0 - Salir \n')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion(1,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '2':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion_con_parametro(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '0':
        os.system('clear') ##Limpia la terminal
    return (estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)

def informes_menu (estaciones,usuarios,bicicletas_en_reparacion):
    print('1 - Usuarios con mayor cantidad de viajes')
    print('2 - Usuarios con mayor duración acumulada de viajes')
    print('3 - Bicicletas en reparación')
    print('4 - Estaciones más activas')
    print('0 - Salir \n')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','4','0']:
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
        os.system('clear') ##Limpia la terminal
    
def ingreso_al_sistema_menu (estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados):
    print('1 - Modificar PIN')
    print('2 - Retirar Bicicleta')
    print('3 - Devolver bicicletas')
    print('0 - Salir \n')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        usuarios,usuarios_bloqueados = modificar_pin(usuarios,usuarios_bloqueados)
    elif opcion == '2':
        estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados = retirar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
    elif opcion == '3':
         estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = validar_ingreso_devolver_bicicleta(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
        
    elif opcion == '0':
        os.system('clear') ##Limpia la terminal
    return estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados
##############################
#####     MAIN CODE      #####
##############################
def menu(estaciones, bicicletas, usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados, bicicletas_en_reparacion):
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
        if opcion == 0:
            seguir = False
        elif opcion == '1':
            estaciones,bicicletas,usuarios =carga_de_datos_menu(estaciones,bicicletas,usuarios)
        elif opcion == '2':
           usuarios,usuarios_bloqueados =  usuarios_menu(usuarios,usuarios_bloqueados)
        elif opcion == '3':
            estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = retiros_automaticos_menu (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
        elif opcion == '4':
            informes_menu(estaciones,usuarios,bicicletas_en_reparacion)
        elif opcion == '5':
            #Ingreso al sistema
            estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados =ingreso_al_sistema_menu(estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados)
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