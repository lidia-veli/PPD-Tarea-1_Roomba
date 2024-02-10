from tkinter import *
#from visualizacion import Ventana
from ventanas import ventana1, calcular_superf_limpiar

root = Tk()
root.geometry("600x400")
root.title('Programa Roomba')

zona1 = (500, 150)  # largo, ancho
zona2 = (480, 101)
zona3 = (309, 480)
zona4 = (90, 220)

zonas = [zona1, zona2, zona3, zona4]

superficie = calcular_superf_limpiar(zonas)

ventana1(root, zonas, superficie)
root.mainloop()
