def carga_datos_automatica():
    #crear 10  estaciones, 5 usuarios, 250 bicis
    #cargar las bicis en las estaciones "a mano"
    cargar_estaciones(estaciones)
    cargar_usuario(usuarios)
    cargar_bicicletas(bicicletas)
    return 0
def carga_datos_random():
    #distribuir 250 bicis aleatoriamente en estaciones
    return 0
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
    for i in range(1,11):
        if i != 1:
            direccion = "Av. Rivadavia {} ".format(numero_direccion + 100) #suma 100mts a la anterior direccion
            #20 segundos = 100mts
            coordenadas = (" {} , {}". format(latitud,(longitud+0.0020)))
            capacidad = 30
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
            for i in range (1,31):
                if(len(estaciones[i][3]) < 30):
                    estaciones[i][3].append(numero_bicicleta)
        bicicletas[i]= [estado,ubicacion]


def cargar_usuario(usuarios):
    pre_nombres = ['Pablo Guarna','Julieta Ponti','Julián Gorge','Ariel Pisterman','Francopre Cuppari']
    pre_celular = ['03034568','03034569','12345678','87654321','13578642'],

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


