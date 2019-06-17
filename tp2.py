from random import randint, random,uniform
import os

def carga_de_datos_menu (estaciones, bicicletas, usuarios):
    print('1 - Carga automática')
    print('2 - Carga automática aleatoria')
    print('0 - Salir')
    opcion = input('Elige una opción para continuar: ')
            
    while opcion not in ['1','2','0']:
        print('La opción es incorrecta.\n')
        opcion = input('Elige una opción para continuar: ')
    if opcion == '1':
        estaciones,bicicletas,usuarios = carga_datos_automatica()
        os.system('clear') ##Limpia la terminal 
        print('Datos cargados!\n')
    elif opcion == '2':
        estaciones,bicicletas,usuarios = carga_datos_random()   
        os.system('clear') ##Limpia la terminal
        print('Datos aleatorios cargados!\n')
    elif opcion == '0':
        os.system('clear') #Limpia la terminal
    return (estaciones, bicicletas, usuarios)

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
    print('0 - Salir')
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
            estaciones,bicicletas,usuarios = carga_de_datos_menu(estaciones, bicicletas, usuarios)
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
# Julian: generar maestro: usuarios con los 4 archivos de usuario, retirar y devolver (TP1), 
# Ariel: Simula muchas veces (agregar distancia recorrida en km) -> Haversigne (geopy)

# Informes.
# Adicionales TP2.
# Guardar usuarios creados en archivo maestro usuarios.
# Generar maestro usuarios con los 4 archivos de usuarios (en cara de que existan).
# Viajes en curso se guardan en archivo binario.
# Al comenzar el programa se finalizan los viajes en curso.
# Roban bici e ingresar al sistema.
# Informe de bicicletas robadas y viajes robadas.