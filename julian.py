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