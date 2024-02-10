def calcular_superf_limpiar(zonas):
    '''Funcion que calcula la superficie total de la habitacion que se puede limpiar.'''
    superficie = 0  # en cm^2
    for zona in zonas:  # zona = (largo, ancho)
        largo, ancho = zona
        superficie += largo*ancho
    print('Superficie:', superficie, 'cm^2')
    # pasar a m^2
    superficie = superficie/10000
    print('Superficie:', superficie, 'm^2')
    return superficie


zona1 = (500, 150)  # largo, ancho
zona2 = (480, 101)
zona3 = (309, 480)
zona4 = (90, 220)

zonas = [zona1, zona2, zona3, zona4]

superficie = calcular_superf_limpiar(zonas)

def calcular_tiempo_limpieza(superficie):
    '''Funcion que calcula el tiempo de limpieza de la habitacion.
    Roomba tiene una velocidad de limpieza de 0.0167 m^2/s.'''
    velocidad = 0.0167  # m^2/s
    # calculamos el tiempo de limpieza
    tiempo = superficie / velocidad  # segundos
    print('Tiempo:', tiempo, 's')

    tiempo = tiempo/60  # minutos
    print('Tiempo:', tiempo, 'minutos')
    return tiempo

calcular_tiempo_limpieza(superficie)
