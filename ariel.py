
def alta_usuario():
    #dni = 0
    #pin = 0
    #nombre_apellido = ""
    #celular = 0
    dni = validar_dni ("Ingrese su DNI: ")
    pin = validar_pin ("Ingrese su pin: ")
    nombre_apellido = validar_nombre_apellido ("Ingrese su nombre y apellido: ")
    celular = validar_celular ("Ingrese su numero de celular: ")
    
    lista_usuarios = [dni, pin, nombre_apellido, celular]
   
    print (lista_usuarios)
def validar_dni (mensaje):
    dni = input (mensaje)
    while  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return dni
    return validar_dni("El DNI es incorrecto, ingreselo nuevamente")    
    

def validar_pin (mensaje):
    pin = input (mensaje)
    while len (pin) ==4 and pin.isdigit() :
        return (pin)
    return validar_pin("ingrese un pin correcto")
    

def validar_nombre_apellido (mensaje):
    nombre_apellido = input (mensaje)
    while not nombre_apellido.isdigit():
        return (nombre_apellido)
    return validar_nombre_apellido("Ingrese un nombre y apellido correcto")

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
#bloque principal

#alta_usuario ()

#a
#4) Permitir que un usuario se ingrese al sistema con DNI y PIN, y pueda modificarlo (solicitar
#ingresarlo 2 veces para evitar errores de tipeo)
def ingresar_usuario (usuarios):
    dni = validar_dni("Ingrese su DNI: ")
    pin = validar_pin("Ingrese su pin: ")
    print("confirme su numero de pin")
    pin2 = validar_pin("Reingrese su pin: ")
    while pin != pin2:
        print("Los pins no son iguales, ingreselos nuevamente")
        pin = validar_pin("Ingrese su pin: ")
        pin2 = validar_pin("Reingrese su pin: ")
    existencia_usuario =  validar_usuario(dni,pin,usuarios)
    if existencia_usuario == "existe":
        print ("existe")
        #modificar_usuario(dni,usuarios)
    elif existencia_usuario == "pin incorrecto":
        print("El PIN es incorrecto")
        ingresar_usuario(usuarios)
    elif existencia_usuario == "no existe":
        print("El dni es incorrecto o usted no tiene un usuario")
        ingresar_usuario(usuarios)

        
def validar_usuario(dni,pin,usuarios):
    claves = usuarios.keys()
    if dni in claves:
        while usuarios[dni][1] == pin:
            return "existe"
        return "pin incorrecto"
    return "no existe"



    

#bloque principal

print("Ingresando al sistema " )
usuarios={}
ingresar_usuario(usuarios)


