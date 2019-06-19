#import geopy
#from geopy import distance

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

def merge_usuarios():
    usuarios1 = open('usuarios1.csv','r',encoding = 'utf-8')
    usuarios2 = open('usuarios2.csv','r',encoding = 'utf-8')
    usuarios3 = open('usuarios3.csv','r',encoding = 'utf-8')
    usuarios4 = open('usuarios4.csv','r',encoding = 'utf-8')
    nombre1,celular1,dni1,pin1 = leer_archivo(usuarios1, [0,0,999999999,0])
    nombre2,celular2,dni2,pin2 = leer_archivo(usuarios2,[0,0,999999999,0])
    nombre3,celular3,dni3,pin3 = leer_archivo(usuarios3, [0,0,999999999,0])
    nombre4,celular4,dni4,pin4 = leer_archivo(usuarios4, [0,0,999999999,0])

    maestro_usuarios = open('usuarios.csv','w',encoding = 'utf-8')
    
    
    while dni1 !=999999999 or dni2 !=999999999 or dni3 !=999999999 or dni4 !=999999999:
        menor = min(int(dni1),int(dni2),int(dni3),int(dni4))
        while menor  == dni1 and dni1 !=0:
            linea = "{},{},{},{} \n".format(nombre1,celular1,dni1,pin1)
            maestro_usuarios.write(linea)
            nombre1,celular1,dni1,pin1 = leer_archivo(usuarios1,[0,0,999999999,0])
        while menor  == dni2 and dni2 !=0:
            linea = "{},{},{},{} \n".format(nombre2,celular2,dni2,pin2)
            maestro_usuarios.write(linea)
            nombre2,celular2,dni2,pin2 = leer_archivo(usuarios2,[0,0,999999999,0])
        while menor  == dni3 and dni3 !=0:
            linea = "{},{},{},{} \n".format(nombre3,celular3,dni3,pin3)
            maestro_usuarios.write(linea)
            nombre3,celular3,dni3,pin3= leer_archivo(usuarios3,[0,0,999999999,0])
        while menor  == dni4 and dni4 !=0:
            linea = "{},{},{},{} \n".format(nombre4,celular4,dni4,pin4)
            maestro_usuarios.write(linea)
            nombre4,celular4,dni4,pin4 = leer_archivo(usuarios4,[0,0,999999999,0])
        
    usuarios1.close()
    usuarios2.close()
    usuarios3.close()
    usuarios4.close()
    maestro_usuarios.close()
    

merge_usuarios()