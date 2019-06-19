########################## Mezcla y Orden (por DNI) de Archivos #############################
def leerArchivo(archivo, fin):
    linea = archivo.readline()
    if linea:
        lista = linea.rstrip('\n').split(',')
        return lista
    else:
        return 0,0,fin,0

def grabarMaestro(usuarios,nombre,celular,dni,pin):
    #if(dni != 'dni' and dni != '9999'):
    usuarios.write(nombre +','+ celular +','+ dni +','+ pin + '\n')

#Supongo que no hay DNIs repetidos
def mezclarArchivos(usuarios1, usuarios2, usuarios3, usuarios4, usuarios):
    nombre1,celular1,dni1,pin1 = leerArchivo(usuarios1, '9999')
    nombre2,celular2,dni2,pin2 = leerArchivo(usuarios2, '9999')
    nombre3,celular3,dni3,pin3 = leerArchivo(usuarios3, '9999')
    nombre4,celular4,dni4,pin4 = leerArchivo(usuarios4, '9999')

    while dni1 or dni2 or dni3 or dn4:
        minor = min(dni1, dni2, dni3, dni4)
        while minor == dni1:
            grabarMaestro(usuarios,nombre1,celular1,dni1,pin1)
            nombre1,celular1,dni1,pin1 = leerArchivo(usuarios1, '9999')
        while minor == dni2:
            grabarMaestro(usuarios,nombre2,celular2,dni2,pin2)
            nombre2,celular2,dni2,pin2 = leerArchivo(usuarios2, '9999')
        while minor == dni3:
            grabarMaestro(usuarios,nombre3,celular3,dni3,pin3)
            nombre3,celular3,dni3,pin3 = leerArchivo(usuarios3, '9999')
        while minor == dni4:
            grabarMaestro(usuarios,nombre4,celular4,dni4,pin4)
            nombre4,celular4,dni4,pin4 = leerArchivo(usuarios4, '9999')

#########################################################################

usuarios1 = open("Ecobici/usuarios1.csv","r")
usuarios2 = open("Ecobici/usuarios2.csv","r")
usuarios3 = open("Ecobici/usuarios3.csv","r")
usuarios4 = open("Ecobici/usuarios4.csv","r")

usuarios = open("Ecobici/usuarios.csv","w")

usuarios.write("nombre,celular,dni,pin\n")
mezclarArchivos(usuarios1, usuarios2, usuarios3, usuarios4, usuarios)

usuarios1.close()
usuarios2.close()
usuarios3.close()
usuarios4.close()

usuarios.close()

#######
#######
#######
#######



'''

def retirar_bicicleta(forma_de_uso, dni, estaciones, bicicletas, usuarios, viajes_actuales):
    #retira la bicicleta y muestra la accion al usuario
    estacion = elegir_estacion(forma_de_uso, estaciones)
    numero_bicicleta, numero_anclaje = elegir_anclaje_de_estacion(estacion, estaciones, bicicletas)
    while numero_bicicleta != -1:
        bicicletas[numero_bicicleta][1] = "En circulación"
        estaciones[estacion][3].remove(numero_bicicleta)
        horario_salida = generar_horario_salida()
        viajes_actuales[dni] = [numero_bicicleta, estacion, horario_salida]
        estaciones[estacion][4] += 1
        if forma_de_uso == "manual":
            print("Retire la bicicleta {} de la estación {} en el anclaje {}\n".format(numero_bicicleta, estacion, numero_anclaje+1))
        else:
           print("{} retiro la bicicleta {} de la estación {} ubicada en {}, a las {}\n".format(usuarios[dni][0],numero_bicicleta, estacion,estaciones[estacion][0],horario_salida))

        ## actualizo archivos
        return (estacion, estaciones, bicicletas, usuarios, viajes_actuales)
    print ("No hay bicicletas disponibles, intente en otra estación")
    ## actualizo archivos
    return (estacion, estaciones, bicicletas, usuarios, viajes_actuales)


#
# A retirar_bicicleta y devolver_bicicleta sólo se le debería añadir el update en los archivos csv, pero
# estos no son iguales al TPv1.0, las bicicletas no estan vinculadas con ningun identificador a la estacion
# ¿de dónde las retiro?
#
# En viajes sólo aparecen los finalizados, aparentemente.
#
'''