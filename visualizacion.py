
from tkinter import *


class Ventana(Frame):

    def __init__(self, master=None):
        '''zonas'''
        Frame.__init__(self, master)
        self.master = master

        # config ventana
        self.master.title('Visualización Roomba Limpiando')
        self.master.geometry("560x690")

        # canvas donde se dibujará la habitación
        self.c = Canvas(master=self.master, width=500, height=630)  # Canvas para dibujar
        self.c.pack()
        self.dibujar_zonas()

        # wifget boton
        self.boton_nueva_ventana = Button(master=self.master, text="Abrir Nueva Ventana", command=self.nueva_ventana)
        self.boton_nueva_ventana.pack(pady=15)


    def definir_zona(self, color, x, y, x1, y1):
        '''Dibujar una zona en el canvas.
        - color (str) color de la zona
        - x (int) coordenada x del punto superior izquierdo
        - y (int) coordenada y del punto superior izquierdo
        - x1 (int) coordenada x del punto inferior derecho
        - y1 (int) coordenada y del punto inferior derecho'''

        self.c.create_rectangle(x, y, x1, y1, fill=color, outline='black')

    def dibujar_zonas(self):
        '''Dibuja las zonas en el canvas.'''
        self.definir_zona('light green', 0, 0, 500, 150)
        self.definir_zona('light blue', 0, 150, 101, 630)
        self.definir_zona('wheat', 191, 150, 500, 630)
        self.definir_zona('plum', 101, 410, 191, 630)

    def nueva_ventana(self):
        # Crear una nueva ventana
        nueva_ventana = Toplevel(self.master)
        nueva_ventana.title("Nueva Ventana")

        # Aquí puedes agregar cualquier contenido adicional a la nueva ventana


if __name__ == "__main__":
    # Crear la ventana principal
    root = Tk()

    # Crear la instancia de la clase Ventana dentro de la ventana principal
    app = Ventana(master=root)

    # Ejecutar el bucle principal de la ventana principal
    root.mainloop()
