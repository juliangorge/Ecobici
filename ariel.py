"""
8) Generar una función que
a. Seleccione un usuario que no esté actualmente en viaje ni bloqueado y una estación al azar
b. Intente retirar una bicicleta para el usuario
c. Genere una duración aleatoria de viaje del usuario menor a 90 minutos
d. Devuelva la bicicleta en otra estación (no la misma)
e. Vaya informando de estas acciones por pantalla, por ejemplo:
i. Juan Pérez retiró la bicicleta 1022 de la estación 3 de Las Heras 3255 a las 12:35:25 h.
ii. Juan Pérez devolvió la bicicleta 1022 en la estación 15 de Gallo 224 a las 13:30:12 h. Al
exceder los 60 minutos de uso ha sido bloqueado.
"""
def seleccionar_usuario(usuarios, viajes_actuales):
    usuario_a_viajar = 0
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append([usuario, usuarios[usuario][2]])
    indice_usuario = 0
    while usuario_a_viajar  == 0:
        if lista_usuarios[indice_usuario][1] != None and lista_usuarios[indice_usuario][0] not in viajes_actuales:
            usuario_a_viajar =  lista_usuarios[indice_usuario][0]
        else:
           indice_usuario +=1
    return (usuario_a_viajar)

def simulacion(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    dni = seleccionar_usuario(usuarios,viajes_actuales)
    estacion =randint(1,10)
    
    numero_anclaje = 0
    while numero_anclaje <= len(estaciones[estacion][3]):
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
            horario_salida = str(hora) + ':' + str(minuto)
            print("{} retiro la bicicleta {} de la estación {} ubicada en {}, a las {}\n".format(usuarios[dni][0],numero_bicicleta, estacion,estacion[0],horario_salida))
            viajes_actuales[dni] = [numero_bicicleta, estacion, horario_salida]
            return (estaciones, bicicletas, usuarios, viajes_actuales)
        numero_anclaje += 1     
    print ("No hay bicicleta disponible, intente en otra estacions")
    estacion_devolucion = randint(1,10)
    while estacion_devolucion == estacion :
        estacion_devolucion = randint(1,10)

    devolver_bicicleta(dni,estacion_devolucion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    return 0  

