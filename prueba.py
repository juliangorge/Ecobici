def carga_datos_automatica(estaciones):
    #Libero diccionarios
    estaciones = {}
    
    #Cargo valores a los diccionarios
    estaciones[0] =  'hola'
    return estaciones

def menu():
    estaciones = {}

    estaciones = carga_datos_automatica(estaciones)
    print(estaciones)

menu()
