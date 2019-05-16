"""
def alta_usuario():
    dni = 0
    pin = 0
    nombre_apellido = ""
    celular = 0
    dni = validar_dni (dni)
    pin = validar_pin (pin)
    nombre_apellido = validar_nombre_apellido (nombre_apellido)
    celular = validar_celular (celular)
    
    lista_usuarios = [dni, pin, nombre_apellido, celular]
   
    print (lista_usuarios)
def validar_dni (dni):
    dni = input ("Ingrese su DNI: ")
    while  dni.isdigit() and len (dni) == 7 or len (dni) == 8 :
        return dni
    return validar_dni(dni)    
    

def validar_pin (pin):
    pin = input ("Ingrese su pin: ")
    while len (pin) ==4 and pin.isdigit() :
        return (pin)
    return validar_pin(pin)
    

def validar_nombre_apellido (nombre_apellido):
    nombre_apellido = input ("Ingrese su nombre y apellido: ")
    while not nombre_apellido.isdigit():
        return (nombre_apellido)
    return validar_nombre_apellido(nombre_apellido)

def validar_celular (celular):
    celular = str(input ("Ingrese su numero de celular: "))
    contador_digitos_numericos = 0
    for caracter in celular: 
        if caracter in "123456789()+-0":
            if caracter in "1234567890":
                contador_digitos_numericos +=1
        else: 
            return validar_celular(celular)
    if contador_digitos_numericos >= 8:
        return celular
    else:
        return validar_celular(celular)
#bloque principal

alta_usuario ()
"""

