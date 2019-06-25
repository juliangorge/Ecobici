#import geopy
#from geopy import distance
import pickle
"""
def calcular_distancia():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    #print(distance.distance(newport_ri, cleveland_oh).kilometres)

#calcular_distancia()
def leer_archivo(archivo, vacio):
    linea = archivo.readline() #guarda una cadena de caracteres del archivo
    if linea:
        lista = linea.rstrip().split(",")
        if lista[2] == 'dni':
            return leer_archivo(archivo, vacio)
        return lista[0], lista[1],int(lista[2]),lista[3]
    else:
        return (vacio)
"""
def hola():
    with open("TP2\ejemplo.pkl","rb") as archivo: 
        seguir = True
        while seguir: 
            try:
                data = pickle.load(archivo)
                print(data)
            except EOFError:
                seguir = False

def guardar():
    with open("TP2\ejemplo.pkl","wb") as archivo:
        pkl= pickle.Pickler(archivo) #declaro que archivo usara el pkl
        
        linea_viaje = {41:[0,1,1],20:[2,2,2]}
        pkl.dump(linea_viaje) #convierte la info a binario y lo sube al archivo
guardar()
hola()