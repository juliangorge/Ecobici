################################################################
################################################################
################################################################

#                                GRUPO POLILLA
#
#.-"""""""---,.               n,                                      ..--------..
#\-          ,,'''-..      n   '\.                ,.n           ..--''           )
# \-     . .,;))     ''-,   \     ''.. .'"'. .,-''    .n   ..-''   (( o         _/
#  \- ' ''''':'          ''-.'"|'--_  '     '  ,.--'''..-''         ' ' ' - .  _/
#   \-                       ''->.  \'  ,--. '/' >..''                        _/
#    \                     (,       /  /.  .\ \ ''    ,)                     ./
#     ''.    .  ..         ')          \ .. /         ('          ..       ./
#        ''-... . ._ .__         .''.  //..\\  ,'.            __ _ _,__.--'
#            /' ((    ..'' ' ' '-'  6  \/__\/  ' '- - -' ' ',''   - '\
#           '(.  6,    '..          /.   ''  .'          ,,'     ) )  )
#            '\  \'C_,_   ==,      / '_      _|\       ,'', ,,_.;-' _/
#              '._ ,   ')   E     /'|_ ')()('_' \     C  ,I'''  _.-'
#                 ''''''\ (('   ,/  ''  (()) ''  '-._ _ __---'''
#                        '' '' '    '==='()'=='
#                                   '(       )'    
#                                   '6        '
#                                    \       /
#                                    '       '
#                                    '       '
#                                    '      '
#                                     '    '
#                                      '..'



################################################################
################################################################
################################################################

def carga_datos_automatica():
    #crear 10  estaciones, 5 usuarios, 250 bicis
    #cargar las bicis en las estaciones "a mano"
    
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    
    #Cargo valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas(estaciones, bicicletas)

    #Imprimo datos
    print(estaciones,'\n')
    print(bicicletas,'\n')
    print(usuarios,'\n')

def carga_datos_random():
    #distribuir 250 bicis aleatoriamente en estaciones
    
    #Libero diccionarios
    estaciones = {}
    bicicletas = {}
    usuarios = {}
    
    #Cargo valores a los diccionarios
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas_random(estaciones, bicicletas)

    #Imprimo datos
    print(estaciones,'\n')
    print(bicicletas,'\n')
    print(usuarios,'\n')

def alta_usuario():
    #validar datos ingresados segun la entidad usuario. permite modificar usuario
    return 0
def modificar_pin():
    #solicitar dni y pin (2 veces). permite modificar pin
    return 0
def desbloquear_usuario():
    #muestra lista de usuarios bloqueados, elegir el usuario, ingresar palabra secreta 
    # y generar un pin aleatorio nuevo
    return 0
def retirar_bicicleta():

    return 0
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

        usuarios[dni] = [nombre,celular,dni,pin]

def mostrar_bicicletas(bicicletas):
    for bici in bicicletas:
        print (bici, bicicletas[bici])



### MAIN
import os

def menu():
    while True:
        print('1 - Carga de datos')
        print('2 - Usuarios')
        print('3 - Retiros automáticos')
        print('4 - Informes')
        print('0 - Salir \n')

        #Probar validación, qué pasa si envío valor vacío o alfanumerico
        opcion = int(input('Elige una opción para continuar: '))

        #tiene que poder volver al menu anterior?
        if opcion == 1:
            print('a - Carga automática')
            print('b - Carga automática aleatoria\n')

            #Probar validación, qué pasa si envío valor vacío o alfanumerico
            opcion = input('Elige una opción para continuar: ')
            if opcion == 'a':
                carga_datos_automatica()
            elif opcion == 'b':
                carga_datos_random()
            #else:
            #   return 0
                #Error y volver

        elif opcion == 2:
            print('a - Listado')
            print('b - Alta')
            print('c - Modificación')
            print('d - Desbloquear\n')
        elif opcion == 3:
            print('a - Viaje aleatorio')
            print('b - Viajes aleatorios múltiples\n')
        elif opcion == 4:
            print('a - Usuarios con mayor cantidad de viajes')
            print('b - Usuarios con mayor duración acumulada de viajes')
            print('c - Bicicletas en reparación')
            print('d - Estaciones más activas\n')
        elif opcion == 5:
            ##Ingreso al sistema
            '''
                El ingreso al sistema muestra un nuevo menú:
                ​Top 10 de usuarios de bicicleta, por cantidad de viajes
                ​Top 5 de usuarios de bicicleta, por duración acumulada de los viajes
                ​Listado de estaciones que tienen bicicletas que necesitan reparación, incluyendo esta
                1. Modificar PIN
                2. Retirar Bicicleta
                3. Devolver Bicicleta
                4. Salir
            '''
        elif opcion == 0:
            return False
        else:
            ##Error volver a ingresar al búcle
            print('Vuelva a intentarlo')


### Inicio
os.system('clear') ##Limpia la terminal
print('¡Bienvenido!\n')
menu()