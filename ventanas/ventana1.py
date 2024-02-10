from tkinter import *
from ventanas.ventana2 import ventana2


def ventana1(root, zonas, superficie):
    '''Funcion que crea la ventana de inicio de la aplicacion.'''

    # widget texto
    h1 = Label(root, text="Bienvenido al programa de Roomba")
    h1.pack(pady=80)
    h1.config(font=15)

    # widget texto
    p1 = Label(root, text=f"La habitación que quiere limpiar tiene {superficie} metros cuadrados \nde superficie accesible por Roomba.")
    p1.pack(pady=15)
    p1.config(font=5)

    # widget boton
    boton = Button(root, text="Ver habitación", command= lambda: ventana2(root, zonas, superficie))
    boton.pack(pady=15)


def calcular_superf_limpiar(zonas):
    '''Funcion que calcula la superficie total de la habitacion que se puede limpiar.'''
    superficie = 0  # en cm^2
    for zona in zonas:  # zona = (largo, ancho)
        largo, ancho = zona
        superficie += largo*ancho
    
    # pasar a m^2
    superficie = superficie/10000
    return superficie
