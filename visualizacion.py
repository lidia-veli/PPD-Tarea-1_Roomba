
from time import sleep
from tkinter import *

class Ventana(Frame):

    def __init__(self, master=None, zonas=[]):
        '''zonas'''
        r = Tk()
        r.title('Visualización Roomba Limpiando')
        self.c = Canvas(master=r, width=500, height=630)  # Canvas para dibujar
        self.c.pack()
        self.dibujarZonas(zonas) 

    def dibujarZonas(self, zonas):
        '''Dibuja las zonas en el canvas.'''
        for zona in zonas:
            x, y, largo, ancho = zona
            self.zona('light blue', x, y, x+largo, y+ancho)

    def zona(self, color, x, y, x1, y1):
        '''Dibujar una zona en el canvas.
        
        INPUT:
        color: str, color de la zona
        x: int, coordenada x del punto superior izquierdo
        y: int, coordenada y del punto superior izquierdo
        x1: int, coordenada x del punto inferior derecho
        y1: int, coordenada y del punto inferior derecho'''
        self.c.create_rectangle(x, y, x1, y1, fill=color, outline=color)

    def acabar(self):
        mainloop()


# Creamos una instancia de la clase Ventana y la asignamos a la variable "ventana"
ventana = Ventana()

# Dibujamos las diferentes zonas que conforman la habitación
ventana.zona('light green', 0, 0, 500, 150)
ventana.zona('light blue', 0, 150, 101, 630)
ventana.zona('wheat', 191, 150, 500, 630)
ventana.zona('plum', 101, 410, 191, 630)

# Terminamos la ventana
ventana.acabar()


# Función que calcula el área de un rectángulo en metros cuadrados
def calculo_area(b, h): #b: base, h: altura
    area = b * h # Multiplicamos la base por la altura para obtener el área en cm2
    area = area/100 # Convertimos el área a m2
    return area

# Función que calcula el tiempo que tarda la Roomba en limpiar una zona en minutos
def calculo_tiempo(a, v): #a: area, v: velocidad
    tiempo = a
