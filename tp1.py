from random import randint, random,uniform
import os

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
    while not dni in usuarios:
        pin = validar_pin ("Ingrese su pin: ")
        nombre = validar_nombre ("Ingrese su nombre y apellido: ")
        celular = validar_celular ("Ingrese su numero de celular: ")
        duracion_viaje = 0
        cantidad_viajes =0
        usuarios[dni] = [nombre,celular,pin,duracion_viaje, cantidad_viajes]
        print(usuarios)
        return(usuarios)
    print("Usted ya tiene un usuario")
    return(usuarios)    
def validar_dni (mensaje):
    dni = input (mensaje)
    while  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return int(dni)
    return validar_dni("El DNI es incorrecto, ingreselo nuevamente: ")    

###########
#### VALIDAR QUE EL DNI EXISTE

def validar_pin (mensaje):
    pin = input (mensaje)

    while len (pin) == 4 and pin.isdigit() :
        return int(pin)
    return validar_pin("Ingrese un pin correcto: ")

def bloquear_usuario(dni,usuarios,usuarios_bloqueados):
    usuarios_bloqueados.append(dni)
    usuarios[dni][2] = None
    print('Usuario bloqueado!')
    return (usuarios,usuarios_bloqueados)

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
        #print ("Bienvenido ", usuarios[dni[0]])
        usuarios = modificar_pin(dni,usuarios)
        print(usuarios)
        return (usuarios) 
    elif existencia_usuario == "pin incorrecto":
        print("El PIN es incorrecto")
        return ingresar_usuario(usuarios)
    elif existencia_usuario == "no existe":
        print("El dni es incorrecto o usted no tiene un usuario")
        return ingresar_usuario(usuarios)
      
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
    for usuario in usuarios_bloqueados:
        print (usuario)
    usuario_a_desbloquear = validar_dni('Ingrese el dni del usuario a desbloquear: ')

    if usuario_a_desbloquear in usuarios_bloqueados:
        palabra_secreta = input ("Ingrese la palabra secreta: ")
        if palabra_secreta == 'shimano': 
            print ("Su usuario ha sido desbloqueado.")
            usuarios_bloqueados.remove(usuario_a_desbloquear)
            usuarios[usuario_a_desbloquear][2] = randint(1000,9999)
            print('Su nuevo pin es: ',usuarios[usuario_a_desbloquear][2])
            return usuarios, usuarios_bloqueados
        else: 
            palabra_secreta = input ("La clave ha sido incorrecta. Ingresela nuevamente: ")
    else:
        print ("Su usuario no está bloqueado.")
        return(usuarios, usuarios_bloqueados)
    
#Sólo cuenta las veces que entra a validar: en 3 -> BLOQUEAR
def validar_bloqueo(usuarios):
    dni = validar_dni("Ingrese su DNI: ")
    claves_usuarios = usuarios.keys()
    while not dni in claves_usuarios:
        print("El usuario no existe, ingrese un usuario valido ")
        return validar_bloqueo(usuarios)
    #Considerando el primer INGRESO como intento nº1
    intentos = 2
    pin = validar_pin("Ingrese su pin: ")
    while usuarios[dni][2] != pin:
        if(intentos <= 3):
            intentos += 1
            pin = validar_pin("Su pin es incorrecto. Ingreselo nuevamente: ")
        else:   
            usuarios = bloquear_usuario(dni,usuarios,usuarios_bloqueados)
            return (usuarios)
    return(usuarios,dni)
##verificar si existe estacion

def retirar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
    usuarios,dni = validar_bloqueo(usuarios)
    if(len(viajes_actuales) and len(viajes_actuales[dni]) > 0):
        print('Usted ya tiene una bicicleta!')
    else:
        if(dni not in usuarios_bloqueados):
            estacion = input('Seleccione número de estación: ')
            claves = estaciones.keys()
            while not int(estacion) in claves or not estacion.isdigit():
                estacion = input('Seleccione un número de estación correcto: ')
            estacion = int(estacion)
            
            numero_anclaje = 0
            while len(estaciones[estacion][3]) >= numero_anclaje:
                if(len(estaciones[estacion][3]) > 0):
                    numero_bicicleta = estaciones[estacion][3][0]
                    if(bicicletas[numero_bicicleta][0] == "ok"):
                        bicicletas[numero_bicicleta][1] = "En circulación"
                        estaciones[estacion][3].remove(numero_bicicleta)
                        print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje))
                        numero_anclaje = 31 #Salgo de while

                        hora = randint(0,22)
                        if(hora == 22):
                            minuto = randint(0,30) 
                        else:
                            minuto = randint(0,59)

                        horario_salida = str(hora) + ':' + str(minuto)

                        viajes_actuales[dni] = [numero_bicicleta, estacion, horario_salida]
                        estaciones[estacion][4] += 1
                        
                        return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
                else:
                    print ("No hay bicicleta disponible, intente en otra estación")
                numero_anclaje += 1
    return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)

def viaje_aleatorio():
    return 0
def viaje_aleatorio_multiple():
    return 0       
def devolver_bicicleta(dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):

    while len(estaciones[estacion][3]) < estaciones[estacion][2]:
        duracion_viaje = randint(5,75)
        if duracion_viaje > 60:
            bloquear_usuario(dni,usuarios,usuarios_bloqueados)
        necesita_reparacion = input("¿La bicicleta necesita reparacion? si/no: ")
        while necesita_reparacion != "si" and necesita_reparacion!= "no":
            necesita_reparacion = input("¿La bicicleta necesita reparacion? si/no: ")
        numero_bicicleta = viajes_actuales[dni][0]
        if necesita_reparacion == "si":
            bicicletas[numero_bicicleta][0] = "reparacion"
        bicicletas[numero_bicicleta][1] = "anclada"

        horario = viajes_actuales[dni][2].split(':')
        hora = int(horario[0])
        minuto = int(horario[1])
        if( (minuto + duracion_viaje ) >= 60 ):
            minuto += (duracion_viaje - 60)
            hora += 1
        else:
            minuto += duracion_viaje

        if minuto <10:
            horario_llegada = str(hora) + ': 0' + str(minuto)
        else:
            horario_llegada = str(hora) + ':' + str(minuto)
        del viajes_actuales[dni]
        
        usuarios[dni][3] += duracion_viaje
        usuarios[dni][4] += 1
        estaciones[estacion][3].append(numero_bicicleta)
        viajes_finalizados[dni] = [numero_bicicleta, horario_llegada, estacion]
        estaciones[estacion][4] += 1 
        if duracion_viaje > 60:
                print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}. Al exceder los 60 minutos de uso ha sido bloqueado.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_llegada))
        else:
            print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_llegada))
            
        return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)

    print("No hay anclajes disponibles.\n")

def seleccionar_usuario(usuarios, viajes_actuales):
    usuario_a_viajar = 0
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][2]])
    indice_usuario = 0
    if (len(usuarios) == 0):
        print("No hay usuarios")
    else: 
        while usuario_a_viajar  == 0:
            indice_usuario = randint(0,(len(lista_usuarios)-1))
            if lista_usuarios[indice_usuario][1] != None and lista_usuarios[indice_usuario][0] not in viajes_actuales and indice_usuario <= len(usuarios):
                usuario_a_viajar =  lista_usuarios[indice_usuario][0]
            #else:
            #   indice_usuario +=1
        return (usuario_a_viajar)
def simulacion(cantidad_ejecuciones,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    
    for numero_ejecucion in range(0,int(cantidad_ejecuciones)):
        dni = seleccionar_usuario(usuarios,viajes_actuales)
        estacion =randint(1,10)
        #saco bici
        if(len(viajes_actuales) and len(viajes_actuales[dni]) > 0):
            print('Usted ya tiene una bicicleta!')
        else:
            numero_anclaje = 0
            while len(estaciones[estacion][3]) >= numero_anclaje:
                if(len(estaciones[estacion][3]) > 0):
                    numero_bicicleta = estaciones[estacion][3][0]
                    if(bicicletas[numero_bicicleta][0] == "ok"):
                        bicicletas[numero_bicicleta][1] = "En circulación"
                        estaciones[estacion][3].remove(numero_bicicleta)
                        
                        numero_anclaje = 31 #Salgo de while

                        hora = randint(0,22)
                        if(hora == 22):
                            minuto = randint(0,30) 
                        else:
                            minuto = randint(0,59)
                        if minuto <10:
                            horario_salida = str(hora) + ': 0' + str(minuto)
                        else:
                            horario_salida = str(hora) + ':' + str(minuto)
                        #horario_salida = str(hora) + ':' + str(minuto)
                        estaciones[estacion][4] +=1
                        print (numero_ejecucion+1)
                        print("{} retiro la bicicleta {} de la estación {} ubicada en {}, a las {}\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_salida))
                        viajes_actuales[int(dni)] = [numero_bicicleta, estacion, horario_salida]    
                else:
                    print ("No hay bicicleta disponible, intente en otra estación")
                numero_anclaje += 1

            estacion_devolucion = estacion
            while estacion_devolucion == estacion  and len(estaciones[estacion_devolucion][3]) >= estaciones[estacion_devolucion][2]:
                estacion_devolucion = randint(1,10)
            #devuelvo bici
            #devolver_bicicleta(dni,estacion_devolucion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
            seguir = True
            while len(estaciones[estacion_devolucion][3]) < estaciones[estacion_devolucion][2] and seguir  ==True:
                duracion_viaje = randint(5,75)
                if duracion_viaje > 60:
                    bloquear_usuario(dni,usuarios,usuarios_bloqueados)
                
                numero_bicicleta = viajes_actuales[dni][0]
                bicicletas[numero_bicicleta][1] = "anclada"

                horario = viajes_actuales[dni][2].split(':')
                hora = int(horario[0])
                minuto = int(horario[1])
                if( (minuto + duracion_viaje ) >= 60 ):
                    minuto += (duracion_viaje - 60)
                    hora += 1
                else:
                    minuto += duracion_viaje

                if minuto <10:
                    horario_llegada = str(hora) + ': 0' + str(minuto)
                else:
                    horario_llegada = str(hora) + ':' + str(minuto)
                del viajes_actuales[dni]
                
                usuarios[dni][3] += duracion_viaje
                usuarios[dni][4] += 1
                estaciones[estacion_devolucion][3].append(numero_bicicleta)
                viajes_finalizados[dni] = [numero_bicicleta, horario_llegada, estacion]
                estaciones[estacion_devolucion][4] += 1 
                if duracion_viaje > 60:
                        print(" {} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}. Al exceder los 60 minutos de uso ha sido bloqueado.\n".format(usuarios[dni][0],numero_bicicleta, estacion_devolucion,estaciones[estacion][0],horario_llegada))
                else:
                    print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}.\n".format(usuarios[dni][0],numero_bicicleta, estacion_devolucion,estaciones[estacion][0],horario_llegada))
                seguir =False        
            if len(estaciones[estacion_devolucion][3]) >= estaciones[estacion_devolucion][2]:
                print("No hay anclajes disponibles")
                seguir = False
    return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    
def simulacion_con_parametro(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    cantidad_ejecuciones_simulacion = input("Ingrese la cantidad de simulaciones: ")
    while not cantidad_ejecuciones_simulacion.isdigit():
        cantidad_ejecuciones_simulacion = input("Ingrese una cantidad de simulaciones valida: ")

    estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion(cantidad_ejecuciones_simulacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    return (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)

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
                print(estaciones[numero_estaciones])

            bicicletas[numero_bicicleta] = [estado, ubicacion]

def cargar_bicicletas_random(estaciones, bicicletas):
    for numero_bicicleta in range(1000,1251):
        if numero_bicicleta < 1241:
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

def informe_duracion_viajes (usuarios):
    usuarios_top_cinco = []
    claves_usuarios = usuarios.keys()
    #usuarios[dni][3] --> duracion de los viajes del usuario
    for usuario in claves_usuarios:
        usuarios_top_cinco.append([usuario, usuarios[usuario][0], usuarios[usuario][3]])
    usuarios_top_cinco.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,5):
        print ((i+1), "-", usuarios_top_cinco[i][1], '(' , usuarios_top_cinco[i][0], ') con' , usuarios_top_cinco[i][2], "minutos\n")

def informe_cantidad_viajes(usuarios):
    usuarios_top_diez = []
    #usuarios[dni][4] --> cantidad viajes usuario
    for usuario in usuarios:
        usuarios_top_diez.append([usuario, usuarios[usuario][0], usuarios[usuario][4]])
    usuarios_top_diez.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,len(usuarios_top_diez)):
        if(i <= 10):
            print ((i+1), "-", usuarios_top_diez[i][1], '(' , usuarios_top_diez[i][0] , ') con' , usuarios_top_diez[i][2], "viajes\n")

def bicicletas_reparacion(bicicletas_en_reparacion):
    print('Bicicletas en reparación: {}\n'.format(len(bicicletas_en_reparacion)))
    for bicicleta in bicicletas_en_reparacion:
        print(bicicleta)

def top_estaciones (estaciones):
    top_estaciones_activas = []
    claves_estaciones = estaciones.keys()
    for estacion in claves_estaciones:
        top_estaciones_activas.append([estacion, estaciones[estacion][4]])
    top_estaciones_activas.sort (key = lambda estacion:estacion[1], reverse = True)
    for i in range (0,10):
        print ((i+1) , "- Estacion: #" , top_estaciones_activas[i][0], 'con', top_estaciones_activas[i][1], 'usos')
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

        elif opcion == '2':
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
                usuarios = ingresar_usuario(usuarios)
            elif opcion == '4':
                usuarios,usuarios_bloqueados =desbloquear_usuario(usuarios, usuarios_bloqueados)
            elif opcion == '0':
                os.system('clear') ##Limpia la terminal

        elif opcion == '3':
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

        elif opcion == '4':
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

        elif opcion == '5':
            ##Ingreso al sistema
            print('1 - Modificar PIN')
            print('2 - Retirar Bicicleta')
            print('3 - Devolver bicicletas')
            print('0 - Salir \n')

            opcion = input('Elige una opción para continuar: ')
            while opcion not in ['1','2','3','0']:
                print('La opción es incorrecta.\n')
                opcion = input('Elige una opción para continuar: ')
            if opcion == '1':
                usuarios = ingresar_usuario(usuarios)
            elif opcion == '2':
                estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados = retirar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
            elif opcion == '3':
                dni = validar_dni("Ingrese su numero de dni: ")
                while not dni in usuarios:
                    dni = validar_dni("DNI incorrecto. Vuelva a ingresarlo: " )

                if(len(viajes_actuales) and len(viajes_actuales[dni]) > 0):
                    estacion = int(input('Seleccione número de estación: '))

                    #Verificar estación
                    claves = estaciones.keys()
                    while not estacion in claves:
                        estacion = int(input('Seleccione número de estación: '))
                    devolver_bicicleta(dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
                else:    
                    print('No tienes ninguna bicicleta para devolver!')
            elif opcion == '0':
                os.system('clear') ##Limpia la terminal
        else:
            os.system('clear') ##Limpia la terminal
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