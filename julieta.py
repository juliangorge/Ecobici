def lectura_usuarios_bloqueados():
    archivo = open(usuarios_bloqueados.csv,'r', encoding='utf-8')
    vacio = []
    bloqueados = []
    lista = leer_archivo(archivo,vacio)
    while lista:
        bloqueados.append(lista[0])
        lista = leer_archivo(archivo,vacio)
    archivo.close()
    return bloqueados
    
def leer_archivo(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        return (lista)
    else:
        return (vacio)
  
def desbloquear_usuario(usuarios):
    bloqueados = lectura_usuarios_bloqueados
#Lista a los usuarios bloqueados y permite desbloquear el usuario
    for usuario in bloqueados:
        print (usuario, usuarios[usuario][0])
    usuario_a_desbloquear = validar_dni('Ingrese el dni del usuario a desbloquear: ')
    if usuario_a_desbloquear in bloqueados:
        palabra_secreta = input ("Ingrese la palabra secreta: ")
        while not palabra_secreta == 'shimano':    
            palabra_secreta = input ("La clave ha sido incorrecta. Ingresela nuevamente: ")
        print ("Su usuario ha sido desbloqueado.")
        bloqueados.remove(usuario_a_desbloquear)
        usuarios[usuario_a_desbloquear][2] = randint(1000,9999) #asigno nuevo pin
        print('Su nuevo pin es: ',usuarios[usuario_a_desbloquear][2])
        return usuarios, bloqueados    
    else:

        print ("Su usuario no está bloqueado.")
        return usuarios, bloqueados

def viajes_en_curso (viaje_en_curso):
    #pickle
    import pickle
    #para abrir en modo binario es con la b al lado del
    with open("viajes_en_curso.pkl,"wb") as archivo:
        pkl= pickle.Pickler(archivo) #declaro que archivo usara el pkl
        pkl.dump(viaje_en_curso) #convierte la info a binario y lo sube al archivo
    print("Se subio la info en modo binario al archivo")
    