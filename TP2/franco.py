from haversine import haversine, Unit
lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

distancia = haversine(lyon, paris,unit = Unit.KILOMETERS)
print(distancia)