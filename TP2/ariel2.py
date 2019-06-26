from random import randint, random,uniform
import os
import pickle

def devolver_bicicletas_inicio(estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    data = []
    with open(r"TP2\viajes_en_curso.pkl","rb") as archivo: 
        seguir = True
        while seguir: 
            try:
                data = pickle.load(archivo)    
            except EOFError:
                seguir = False
                
    print(data)            
    bicicletas_devueltas = []
    
    for viaje in data:
        print(viaje)
        viajes_actuales[int(viaje[0])] = [int(viaje[1]),int(viaje[2]),viaje[3]]
        print(viajes_actuales)
        devolver_bicicleta("simulacion", int(viaje[0]), int(viaje[1]), estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
        bicicletas_devueltas.append(viaje[0])
    
    return estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados, bicicletas_devueltas
    


def lectura_estaciones():
    lista_estaciones = recorrer_archivo(r'TP2\estaciones.csv')
    estaciones = {}
    
    for datos_estacion in lista_estaciones:
        cantidad_usos_estacion = 0
        #longitud,latitud,direccion,capacidad, bicicletas_ancladas, cantidad_usos
        estaciones[int(datos_estacion[3])] = [datos_estacion[0],datos_estacion[1],datos_estacion[2],datos_estacion[4], [],cantidad_usos_estacion]
    return estaciones

def lectura_bicicletas(estaciones):
    lista_bicicletas = recorrer_archivo(r'TP2\bicicletas.csv')
    bicicletas = {}
    #estado,ubicacion
    estado  = "ok"
    ubicacion = "anclada"
    for datos_bicicleta in lista_bicicletas:
        numero_bicicleta = int(datos_bicicleta[1])
        bicicletas[numero_bicicleta] = [estado,ubicacion]
    return bicicletas, estaciones    

def anclar_bicicletas(bicicletas, estaciones, bicicletas_devueltas):
    numeros_estaciones =[]
    for estacion in estaciones:
        numeros_estaciones.append(int(estacion))
    longitud_numeros_estaciones = len(numeros_estaciones) - 1
    for bicicleta in bicicletas:
        if not bicicleta in bicicletas_devueltas:
            posicion_estacion = randint(0,longitud_numeros_estaciones)
            numero_estacion = numeros_estaciones[posicion_estacion]
            while len(estaciones[numero_estacion][4]) >= 29:
                posicion_estacion = randint(0,longitud_numeros_estaciones)
                numero_estacion = numeros_estaciones[posicion_estacion]
            estaciones[numero_estacion][4].append(bicicleta) 
    return bicicletas,estaciones

def carga_datos_automatica(estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    
    estaciones =  lectura_estaciones()
    bicicletas, estaciones = lectura_bicicletas (estaciones)
    print("datos cargados!")
    estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados, bicicletas_devueltas= devolver_bicicletas_inicio(estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    try:
        usuarios, usuarios_bloqueados = lectura_usuarios(usuarios_bloqueados)
    except FileNotFoundError:
        merge_usuarios()
        usuarios, usuarios_bloqueados = lectura_usuarios(usuarios_bloqueados)

    bicicletas, estaciones= anclar_bicicletas(bicicletas, estaciones, bicicletas_devueltas)
    
    return estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados

def leer_archivo_usuarios(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        if lista[2] == 'dni':
            return leer_archivo_usuarios(archivo, vacio)
        return lista[0], lista[1],int(lista[2]),lista[3]
    else:
        return (vacio)

def merge_usuarios():
    usuarios1 = open(r'TP2\usuarios1.csv','r',encoding = 'utf-8')
    usuarios2 = open(r'TP2\usuarios2.csv','r',encoding = 'utf-8')
    usuarios3 = open(r'TP2\usuarios3.csv','r',encoding = 'utf-8')
    usuarios4 = open(r'TP2\usuarios4.csv','r',encoding = 'utf-8')
    nombre1,celular1,dni1,pin1 = leer_archivo_usuarios(usuarios1, [0,0,999999999,0])
    nombre2,celular2,dni2,pin2 = leer_archivo_usuarios(usuarios2,[0,0,999999999,0])
    nombre3,celular3,dni3,pin3 = leer_archivo_usuarios(usuarios3, [0,0,999999999,0])
    nombre4,celular4,dni4,pin4 = leer_archivo_usuarios(usuarios4, [0,0,999999999,0])

    maestro_usuarios = open(r'TP2\maestro_usuarios.csv','w',encoding = 'utf-8')
    linea_inicio_usuarios = "nombre,celular,dni,pin"
    maestro_usuarios.write(linea_inicio_usuarios)
    while dni1 !=999999999 or dni2 !=999999999 or dni3 !=999999999 or dni4 !=999999999:
        menor = min(int(dni1),int(dni2),int(dni3),int(dni4))
        while menor  == dni1 and dni1 !=0:
            linea = "{},{},{},{} \n".format(nombre1,celular1,dni1,pin1)
            maestro_usuarios.write(linea)
            nombre1,celular1,dni1,pin1 = leer_archivo_usuarios(usuarios1,[0,0,999999999,0])
        while menor  == dni2 and dni2 !=0:
            linea = "{},{},{},{} \n".format(nombre2,celular2,dni2,pin2)
            maestro_usuarios.write(linea)
            nombre2,celular2,dni2,pin2 = leer_archivo_usuarios(usuarios2,[0,0,999999999,0])
        while menor  == dni3 and dni3 !=0:
            linea = "{},{},{},{} \n".format(nombre3,celular3,dni3,pin3)
            maestro_usuarios.write(linea)
            nombre3,celular3,dni3,pin3= leer_archivo_usuarios(usuarios3,[0,0,999999999,0])
        while menor  == dni4 and dni4 !=0:
            linea = "{},{},{},{} \n".format(nombre4,celular4,dni4,pin4)
            maestro_usuarios.write(linea)
            nombre4,celular4,dni4,pin4 = leer_archivo_usuarios(usuarios4,[0,0,999999999,0])
    usuarios1.close()
    usuarios2.close()
    usuarios3.close()
    usuarios4.close()
    maestro_usuarios.close()

def lectura_usuarios(usuarios_bloqueados):
    lista_usuarios = recorrer_archivo(r'TP2\maestro_usuarios.csv')
    usuarios = {}
    
    for datos_usuario in lista_usuarios:
        #usuarios[dni] = [nombre,celular,pin]
        pin = int(datos_usuario[3])
        dni = int(datos_usuario[2])
        usuarios[dni] = [datos_usuario[0],datos_usuario[1],pin]
        if pin == 0:
            usuarios_bloqueados.append(dni)

    return usuarios, usuarios_bloqueados

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
        linea_usuario_nuevo = "{},{},{},{}".format(nombre,celular,dni,pin)
        
        maestro_usuarios2 = open(r'TP2\maestro_usuarios.csv','a',encoding = 'utf-8')
        maestro_usuarios2.write(linea_usuario_nuevo)
        maestro_usuarios2.close()    
        print("Su usuario ha sido creado.")

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
        cambiar_pin_archivo(dni,pin_nuevo)
        print("Su nuevo pin es: ",pin_nuevo)
    else:
        print("Su usuario esta bloqueado, no puede modificar su pin.")
    return (usuarios,usuarios_bloqueados)

def cambiar_pin_archivo(dni,pin_nuevo):
    archivo_usuarios = open(r'TP2\maestro_usuarios.csv', 'r', encoding = 'utf-8')
    lineas_usuario = archivo_usuarios.readlines()
    archivo_usuarios.close()
    archivo_usuarios = open(r'TP2\maestro_usuarios.csv', 'w', encoding = 'utf-8')
    for linea in lineas_usuario:
        lista_linea = linea.split(",")
        if int(lista_linea[2]) == dni:
            linea= "{},{},{},{}".format(lista_linea[0],lista_linea[1],dni,pin_nuevo)
        archivo_usuarios.write(linea)
    archivo_usuarios.close()

def bloquear_usuario(dni,usuarios,usuarios_bloqueados):
    #Recibe la lista de usuarios bloqueados añade el usuario a bloquear
    usuarios_bloqueados.append(dni)
    usuarios[dni][2] = 0
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

def retirar_bicicleta(forma_de_uso, dni, estaciones, bicicletas, usuarios, viajes_actuales):
    #retira la bicicleta y muestra la accion al usuario
    estacion = elegir_estacion(forma_de_uso, estaciones)
    numero_bicicleta, numero_anclaje = elegir_anclaje_de_estacion(estacion, estaciones, bicicletas)
    while numero_bicicleta != -1:
        bicicletas[numero_bicicleta][1] = "En circulación"
        estaciones[estacion][3].remove(numero_bicicleta)
        horario_salida = generar_horario_salida()
        viajes_actuales[dni] = [numero_bicicleta, estacion, horario_salida,0]
        estaciones[estacion][4] += 1
        if forma_de_uso == "manual":
            print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje+1))
        else:
           
           print("{} retiro la bicicleta {} de la estación {} ubicada en {}, a las {}\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_salida))
        """
        linea_viaje_nuevo = "{},{},{},{}".format(dni, numero_bicicleta,estacion,horario_salida)
        #persistir_retiro_bicicleta(linea_viaje_nuevo)
        archivo_viajes = open(r'TP2\viajes_en_curso.csv', 'a', encoding = 'utf-8')
        archivo_viajes.write(linea_viaje_nuevo) 
        archivo_viajes.close()
        """
        return (estacion,estaciones, bicicletas, usuarios, viajes_actuales)
    print ("No hay bicicletas disponibles, intente en otra estación")
    return (estacion,estaciones, bicicletas, usuarios, viajes_actuales)


    
def simulacion(cantidad_ejecuciones,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    #Simula retiro y devolución de una bicicleta
    for numero_ejecucion in range(0,int(cantidad_ejecuciones)):
        dni = seleccionar_usuario(usuarios,viajes_actuales,usuarios_bloqueados)
        if dni != -1: #si es -1, no hay usuarios disponibles 
            print (numero_ejecucion+1) #muestra el numero de simulacion
            #saco bici
            estacion,estaciones, bicicletas, usuarios, viajes_actuales = retirar_bicicleta("simulacion", dni, estaciones, bicicletas, usuarios, viajes_actuales)
            #busco al azar la estacion a devolver la bicicleta 
            estacion_devolucion = estacion
            while estacion_devolucion == estacion  or len(estaciones[estacion_devolucion][3]) >= estaciones[estacion_devolucion][2]:
                estacion_devolucion = randint(1,10)
             #devuelvo bici
            devolver_bicicleta("simulacion",dni,estacion_devolucion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)              
    return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    
def simulacion_con_parametro(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    #Se ingresa la cantidad de veces que se quiere ejecutar simulacion()
    cantidad_ejecuciones_simulacion = input("Ingrese la cantidad de simulaciones: ")
    while not cantidad_ejecuciones_simulacion.isdigit():
        cantidad_ejecuciones_simulacion = input("Ingrese una cantidad de simulaciones valida: ")

    estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = simulacion(cantidad_ejecuciones_simulacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    return (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)

def informe_cantidad_viajes(usuarios):
    #muestra los 10 usuarios que mas viajes hicieron
    lista_usuarios = []
    #usuarios[dni][4] --> cantidad viajes usuario
    for usuario in usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][0], usuarios[usuario][4]])
    lista_usuarios.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,len(lista_usuarios)):
        if(i <= 10):
            print("{} - {}, ({}) con {} viajes\n".format((i+1), lista_usuarios[i][1], lista_usuarios[i][0], lista_usuarios[i][2]))
def informe_duracion_viajes (usuarios):
    #muestra los 5 usuarios con mas duracion acumulada de viajes
    lista_usuarios = []
    claves_usuarios = usuarios.keys()
    #usuarios[dni][3] --> duracion de los viajes del usuario
    for usuario in claves_usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][0], usuarios[usuario][3]])
    lista_usuarios.sort (key = lambda usuario:usuario[2], reverse = True)
    for i in range (0,5):
        print("{} - {}, ({}) con {} minutos\n".format((i+1), lista_usuarios[i][1], lista_usuarios[i][0], lista_usuarios[i][2]))

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

def retirar_bicicleta_ingreso(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
    #Retira una bicicleta del diccionario estaciones y la pone en circulacion (viajes actuales), verificando que el usuario no esté bloqueado
    usuarios,dni = validar_bloqueo(usuarios,usuarios_bloqueados)
    if dni in viajes_actuales:
        print('Usted ya tiene una bicicleta!')
    else:
        if(dni not in usuarios_bloqueados):
            retirar_bicicleta("manual", dni, estaciones, bicicletas, usuarios, viajes_actuales)
        else:
            print("Usted esta bloqueado, no puede retirar una bicicleta.")
    return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)

def elegir_estacion(forma_a_utilizar, estaciones):
    if(forma_a_utilizar == "manual"):
        estacion = input('Seleccione número de estación: ')
        claves = estaciones.keys()
        while not int(estacion) in claves or not estacion.isdigit():
            estacion = input('Seleccione un número de estación correcto: ')
        estacion = int(estacion)
    else:
        estacion = randint(1,10)
    return estacion

def elegir_anclaje_de_estacion(estacion, estaciones, bicicletas):
    #elije la estacion, la bicicleta y devuelve el numero de la bicicleta, numero de estacion y el anclaje donde esta ubicada
    
    numero_anclaje = 0
    while len(estaciones[estacion][3]) >= numero_anclaje:
        if(len(estaciones[estacion][3]) > 0):
            numero_bicicleta = estaciones[estacion][3][numero_anclaje]
            if(bicicletas[numero_bicicleta][0] == "ok"):
                return numero_bicicleta,numero_anclaje
        else:
            print ("No hay bicicletas, intente en otra estación")
        numero_anclaje += 1
    numero_bicicleta = -1
    return (numero_bicicleta, numero_anclaje)

def generar_horario_salida():
    #devuelve el horario generado al azar del retiro de la bicicleta
    hora = randint(0,22)
    segundos = randint(10,59)
    if(hora == 22):
        minuto = randint(0,30) 
    else:
        minuto = randint(0,59)
    if minuto <10: #agrega el 0 a los minutos si son menores a 10
        horario_salida = str(hora) + ':0' + str(minuto) + str(segundos)
    else:
        horario_salida = str(hora) + ':' + str(minuto) + str(segundos)
    return(horario_salida)

def devolver_bicicleta(forma_de_uso, dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    #Devuelve una bicicleta al diccionario estaciones y la quita de circulacion (viajes actuales), verificando el tiempo. En caso de excederse el usuario debe bloquearse
    if len(estaciones[estacion][4]) <= 29: #se fija que haya lugar en la estacion
        duracion_viaje = randint(5,75)
        if duracion_viaje > 60:
            bloquear_usuario(dni,usuarios,usuarios_bloqueados)
        numero_bicicleta = viajes_actuales[dni][0]
        if forma_de_uso == "manual":
            bicicletas = estado_bicicleta_devolucion(numero_bicicleta,bicicletas)
        else:
            bicicletas[numero_bicicleta][0] = "ok"
            bicicletas[numero_bicicleta][1] = "anclada"

        horario_llegada = generar_horario_llegada(dni, viajes_actuales, duracion_viaje)
        estacion_origen = viajes_actuales[dni][2]
        hora_salida = viajes_actuales[dni][3]
        del viajes_actuales[dni] #borra el viaje actual
        
        estaciones[estacion][4].append(numero_bicicleta)
        viajes_finalizados[dni] = [numero_bicicleta, horario_llegada, estacion]
        estaciones[estacion][5] += 1 
        if duracion_viaje > 60:
            print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}. Al exceder los 60 minutos de uso ha sido bloqueado.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][2],horario_llegada))
        else:
            print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_llegada))
        #estacion_origen,estacion_destino,dni_usuario,hora_retiro,tiempo_de_uso,hora_de_llegada,id_bici
        #hora_salida, estacion_origen = eliminar_registro_viaje(dni)
        linea_viaje_finalizado = "{},{},{},{},{},{},{}".format(estacion_origen, estacion, dni,hora_salida, duracion_viaje, horario_llegada, numero_bicicleta)
        #persistir_viaje_finalizado(linea_viaje_finalizado)
        
        archivo_viajes_finalizados = open(r'TP2\viajes.csv', 'w', encoding = 'utf-8')
        archivo_viajes_finalizados.write(linea_viaje_finalizado)
        archivo_viajes_finalizados.close()
        return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    else:
        print("No hay anclajes disponibles.\n")
    return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)  




def generar_horario_llegada(dni, viajes_actuales, duracion_viaje):
    #recibe los viajes actuales y la duracion del viaje, devuelve el horario de llegada calculado a partir del horario de salida y la duracion
    horario = viajes_actuales[dni][2].split(':')
    hora = int(horario[0])
    minuto = int(horario[1])
    segundos = int(horario[2])
    if( (minuto + duracion_viaje ) >= 60 ):
        minuto += (duracion_viaje - 60)
        hora += 1
    else:
        minuto += duracion_viaje
    #agrega el 0 a los minutos si son menores a 10
    if minuto <10:
        horario_llegada = str(hora) + ':0' + str(minuto) +str(segundos)
    else:
        horario_llegada = str(hora) + ':' + str(minuto) + str(segundos)
    return (horario_llegada)

def estado_bicicleta_devolucion(numero_bicicleta,bicicletas):
    #el usuario ingresa si la bici necesita reparacion o no cuando la devuelve, devuelve el diccionario bicicletas actualizado
    necesita_reparacion = input("¿La bicicleta necesita reparacion? si/no: ")
    while necesita_reparacion != "si" and necesita_reparacion!= "no":
        necesita_reparacion = input("¿La bicicleta necesita reparacion? si/no: ")
    if necesita_reparacion == "si":
        bicicletas[numero_bicicleta][0] = "reparacion"
    bicicletas[numero_bicicleta][1] = "anclada"
    return bicicletas

def validar_ingreso_devolver_bicicleta(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    #pide los datos para devolver la bicicleta, en caso de ser validos y tener una bicicleta, la devuelve
    dni = validar_dni("Ingrese su numero de dni: ")
    while not dni in usuarios:
        dni = validar_dni("DNI incorrecto. Vuelva a ingresarlo: " )
    if dni in viajes_actuales:
        estacion = int(input('Seleccione número de estación: '))
        #Verificar estación
        while not estacion in estaciones:
            estacion = int(input('Seleccione número de estación: '))
        devolver_bicicleta("manual",dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)    
    else:    
        print('No tienes ninguna bicicleta para devolver!')
    return estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados

def robar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
    #Retira una bicicleta del diccionario estaciones y la pone en circulacion (viajes actuales), verificando que el usuario no esté bloqueado
    usuarios,dni = validar_bloqueo(usuarios,usuarios_bloqueados)
    if dni in viajes_actuales:
        print('Usted ya tiene una bicicleta!')
    else:
        if(dni not in usuarios_bloqueados):
            estado, dni_ladron, nombre_ladron = retirar_bicicleta_robando(dni, estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)

            if(dni == dni_ladron):
                if(estado == 'bloqueado'):
                    print('El usuario {} fue bloqueado por intento de robo'.format(nombre_ladron))
                else:
                    print('El usuario {} ha robado una bicicleta!'.format(nombre_ladron))
        else:
            print("Usted esta bloqueado, no puede retirar una bicicleta.")
    return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)

def retirar_bicicleta_robando(dni, estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
    #dni = dni del ladron
    bicicleta = input('Seleccione número de bicicleta: ')
    claves = bicicletas.keys()
    while not int(bicicleta) in claves or not bicicleta.isdigit():
        bicicleta = input('Seleccione un número de bicicleta correcto: ')
    bicicleta = int(bicicleta)

    #Revisar si bicicleta está en viajes actuales, sino bloquear
    bloquear = True
    for datos in viajes_actuales.values():
        if(datos[0] == bicicleta):
            bloquear = False

            #Obtengo DNI del asaltado
            usuario_asaltado = [dni for dni, datos_ in viajes_actuales.items() if datos_[0] == bicicleta]

            #Elimino el viaje actual del asaltado, generando uno identico pero con el DNI del ladron
            del viajes_actuales[usuario_asaltado[0]]
            viajes_actuales[dni] = [ bicicleta, datos[1], datos[2] ]

    for dni_ladron, usuario in usuarios.items():
        if dni == dni_ladron:
            if(bloquear):
                bloquear_usuario(dni_ladron,usuarios,usuarios_bloqueados)
                return 'bloqueado', dni_ladron, usuarios[dni][0]
            else:
                linea_viaje_robado = "{},{},{}".format(bicicleta,usuario_asaltado,dni_ladron)
                archivo_viajes_robados = open(r'TP2/viajes_robados.csv', 'w', encoding = 'utf-8')
                archivo_viajes_robados.write(linea_viaje_robado)
                archivo_viajes_robados.close()
                return 'robo', dni_ladron, usuarios[dni_ladron][0]

def informe_viajes_robados ():
    lista_viajes_robados = recorrer_archivo(r'TP2\viajes_robados.csv')
    for datos_viaje in lista_viajes_robados:
        print("la bicicleta {}, fue robada a {} por {} ").format(datos_viaje[0], datos_viaje[1], datos_viaje[2])
    
def guardar_viajes_en_curso(viajes_actuales):
    with open("viajes_en_curso.pkl","wb") as archivo:
        pkl= pickle.Pickler(archivo) #declaro que archivo usara el pkl
        for viaje in viajes_actuales:
            linea_viaje = "{},{},{},{}".format(viaje,viajes_actuales[viaje][0],viajes_actuales[viaje][1],viajes_actuales[viaje][2])
            pkl.dump(linea_viaje) #convierte la info a binario y lo sube al archivo

def usuarios_menu (usuarios,usuarios_bloqueados):
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
    return (usuarios,usuarios_bloqueados)

def retiros_automaticos_menu (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
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
    return (estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)

def informes_menu (estaciones,usuarios,bicicletas_en_reparacion):
    print('1 - Usuarios con mayor cantidad de viajes')
    print('2 - Usuarios con mayor duración acumulada de viajes')
    print('3 - Bicicletas en reparación')
    print('4 - Estaciones más activas')
    print('5 - Viajes robados')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','4','5','0']:
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
    elif opcion == '5':
        informe_viajes_robados()
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    
def ingreso_al_sistema_menu (estaciones, usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados):
    print('1 - Modificar PIN')
    print('2 - Retirar Bicicleta')
    print('3 - Devolver bicicletas')
    print('4 - Robar bicicleta')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
    while opcion not in ['1','2','3','4','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        usuarios,usuarios_bloqueados = modificar_pin(usuarios,usuarios_bloqueados)
    elif opcion == '2':
        estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados = retirar_bicicleta_ingreso(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
    elif opcion == '3':
        estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = validar_ingreso_devolver_bicicleta(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    elif opcion == '4':
        #robar bici
        estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados = robar_bicicleta(estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
        print("aca se roba la bici")
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    return (estaciones,usuarios,usuarios_bloqueados,bicicletas,bicicletas_en_reparacion,viajes_actuales,viajes_finalizados)

##############################
#####     MAIN CODE      #####
##############################

def menu(estaciones, bicicletas,usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados, bicicletas_en_reparacion):
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
            guardar_viajes_en_curso(viajes_actuales)
            seguir = False
        elif opcion == '1':
            estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados = carga_datos_automatica(estaciones, bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
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
usuarios= {}
usuarios_bloqueados = []
viajes_actuales = {}
viajes_finalizados = {}
bicicletas_en_reparacion = []
### Arranco programa
os.system('clear') ##Limpia la terminal
menu(estaciones, bicicletas,usuarios, usuarios_bloqueados, viajes_actuales, viajes_finalizados, bicicletas_en_reparacion)