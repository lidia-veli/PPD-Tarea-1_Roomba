from tkinter import *


# VENTANA 1 --------------------------------------------------------------------
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



# VENTANA 2 --------------------------------------------------------------------
def ventana2(root, zonas, superficie):

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


# VENTANA 3 --------------------------------------------------------------------
def ventana3(root, superficie):    

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
