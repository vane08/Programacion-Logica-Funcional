#TSP con Hill Climbing
import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) **2 + (lon1 -lon2) **2)

     #Calcular la distancia cubierta por cada ruta.
def evalua_ruta(ruta):
    total = 0
    for i in range(0, len(ruta)-1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total = total + distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[i+1]
    ciudad2 = ruta[0]
    total = total + distancia(coord[ciudad1], coord[ciudad2])
    return total

def hill_climbing():
    #Crear la ruta inicial aleatoria
    ruta = []
    for ciudad in coord:
        ruta.append(ciudad)
    random.shuffle(ruta)
    
    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta) 
    #Evaluar Vecinos 
    for i in range (0, len(ruta)):
        if mejora:
            break 
        for j in range(0, len(ruta)):
            if i!= j:
                ruta_tmp = ruta[:]
                ciudad_tmp = ruta[i]
                ruta_tmp[i] = ruta_tmp[j]
                ruta_tmp[j] = ciudad_tmp
                dist = evalua_ruta(ruta_tmp)
                if dist < dist_actual:
                    #Se ha encontrado un vecino que mejora el resultado.
                    mejora = True
                    ruta = ruta_tmp[:]
                    break 
    return ruta  

if __name__ == "__main__":
    coord = {
        'JiloYork': (19.984146, -99.519127),
        'Toluca': (19.286167856525594, -99.65473296644892),
        'Atlacomulco': (19.796802401380955, -99.87643301629244),
        'Guadalajara': (20.655773344775373, -103.35773871581326),
        'Monterrey': (25.675859554333684, -100.31405053526082),
        'Cancún': (21.158135651777727, -86.85092947858692),
        'Morelia': (19.720961251258654, -101.15929186858635),
        'Aguascalientes': (21.88473831747085, -102.29198705069501),
        'Queretaro': (20.57005870003398, -100.45222862892079),
        'CDMX': (19.429550164848152, -99.13000959477478)
    }
    
    ruta = hill_climbing()
    print(ruta)
    print("Distancia Total: " + str(evalua_ruta(ruta)))
