from tkinter import *


def ventana3(root, superficie):
    '''Funcion que crea la ventana de visualización de tiempo de limpieza.'''   

    vent3 = Toplevel(root)
    vent3.title('Tiempo de limpieza')
    vent3.geometry("600x400")

    # widget texto
    tiempo = calcular_tiempo_limpieza(superficie)
    p1 = Label(vent3, text=(f"Tiempo de limpieza necesario: {tiempo[0]} minutos y {tiempo[1]} segundos."))
    p1.pack(pady=20)
    p1.config(font=15)

    # widget boton
    boton = Button(vent3, text="Terminar", command=lambda: root.destroy())
    boton.pack(pady=30)



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
