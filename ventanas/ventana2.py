from tkinter import *
from ventanas.ventana3 import ventana3


def ventana2(root, zonas, superficie):
    '''Funcion que crea la ventana de visualización de la habitación.'''

    vent2 = Toplevel(root)
    vent2.title('Visualización Habitación')
    vent2.geometry("600x800")

    # widget canvas
    c = Canvas(master=vent2, width=500, height=630)
    c.pack()
    # zonas
    c.create_rectangle(0, 0, 500, 150, fill='light green', outline='black')
    c.create_rectangle(0, 150, 101, 630, fill='light blue', outline='black')
    c.create_rectangle(191, 150, 500, 630, fill='wheat', outline='black')
    c.create_rectangle(101, 410, 191, 630, fill='plum', outline='black')

    # widget boton
    boton = Button(vent2, text="Limpiar", command= lambda: ventana3(root, superficie))
    boton.pack(pady=5)



def calcular_tiempo_limpieza(superficie):
    '''Funcion que calcula el tiempo de limpieza de la habitacion.
    Roomba tiene una velocidad de limpieza de 0.0167 m^2/s.'''
    velocidad = 0.0167  # m^2/s
    # calculamos el tiempo de limpieza
    tiempo = superficie / velocidad  # segundos
    # pasar a minutos y segundos
    min = int(tiempo // 60)
    seg = int(tiempo % 60)

    return min, seg
