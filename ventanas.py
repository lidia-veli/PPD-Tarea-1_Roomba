from tkinter import *
#from visualizacion import Ventana


# VENTANA 1 --------------------------------------------------------------------
def ventana1(root, zonas, superficie):
    '''Funcion que crea la ventana de inicio de la aplicacion.'''

    # widget texto
    h1 = Label(root, text="Bienvenido al programa de Roomba")
    h1.pack(pady=80)
    h1.config(font=15)

    # widget texto
    p1 = Label(root, text=f"La habitación que quiere limpiar tiene {superficie} metros cuadrados de superficie accesible por Roomba.")
    p1.pack(pady=20)
    p1.config(font=15)

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
    vent2.geometry("560x690")

    # widget texto
    p1 = Label(vent2, text="Habitación")
    p1.pack(pady=20)
    p1.config(font=10)

    # widget boton
    boton = Button(vent2, text="Limpiar", command= lambda: ventana3(root, superficie))

    boton.pack(pady=15)



def calcular_tiempo_limpieza(superficie):
    '''Funcion que calcula el tiempo de limpieza de la habitacion.
    Roomba tiene una velocidad de limpieza de 0.0167 m^2/s.'''
    velocidad = 0.0167  # m^2/s
    # calculamos el tiempo de limpieza
    tiempo = superficie / velocidad  # segundos
    tiempo = tiempo/60  # minutos

    return tiempo


# VENTANA 3 --------------------------------------------------------------------
def ventana3(root, superficie):    

    vent3 = Toplevel(root)
    vent3.geometry("560x690")

    # widget texto
    tiempo = calcular_tiempo_limpieza(superficie)
    p1 = Label(vent3, text=(f"Tiempo final de limpieza: {tiempo} minutos."))
    p1.pack(pady=20)
    p1.config(font=15)

    # widget boton
    boton = Button(vent3, text="Terminar", command=lambda: root.destroy())
    boton.pack(pady=30)
