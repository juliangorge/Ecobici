def devolver_bicicleta(forma_de_uso, dni,estacion,estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados):
    #Devuelve una bicicleta al diccionario estaciones y la quita de circulacion (viajes actuales), verificando el tiempo. En caso de excederse el usuario debe bloquearse
    if len(estaciones[estacion][3]) < estaciones[estacion][2]: #se fija que haya lugar en la estacion
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
        del viajes_actuales[dni] #borra el viaje actual
        usuarios[dni][3] += duracion_viaje
        usuarios[dni][4] += 1
        estaciones[estacion][3].append(numero_bicicleta)
        viajes_finalizados[dni] = [numero_bicicleta, horario_llegada, estacion]
        estaciones[estacion][4] += 1 
        if duracion_viaje > 60:
            print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}. Al exceder los 60 minutos de uso ha sido bloqueado.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_llegada))
        else:
            print("{} devolvio la bicicleta {} en la estación {} ubicada en {}, a las {}.\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_llegada))


        viajes = open('viajes.csv','r',encoding = 'utf-8')

        #estacion_destino = estacion
        linea = "{},{},{},{},{},{},{} \n".format(estaciones[estacion][3],estacion,dni,viajes_actuales[dni][3],duracion_viaje,horario_llegada,numero_bicicleta)
        viajes.write(linea)
        viajes.close()

        return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)
    else:
        print("No hay anclajes disponibles.\n")
    return(estaciones,bicicletas,usuarios,usuarios_bloqueados,viajes_actuales,viajes_finalizados)  

################################################################################################


# ROBAR BICi
# ROBAR BICi
# ROBAR BICI

def retirar_bicicleta_robando(dni, estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados):
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

    for dni_, usuario in usuarios.items():
        if dni == dni_:
            if(bloquear):
                bloquear_usuario(dni,usuarios,usuarios_bloqueados)
                return 'bloqueado', dni_, usuarios[dni][0]
            else:
                return 'robo', dni_, usuarios[dni][0]

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
                    print('El usuario ',nombre_ladron,'fue bloqueado por intento de robo')
                else:
                    print('El usuario ',nombre_ladron,'ha robado una bicicleta!')

        else:
            print("Usted esta bloqueado, no puede retirar una bicicleta.")
    return (estaciones, bicicletas, usuarios, viajes_actuales, usuarios_bloqueados)
# ROBAR BICI