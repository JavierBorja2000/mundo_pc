from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

print("   :ORDEN:")
ordenes = list()
while True: 
    while True:
        nombre = input("Ingrese el nombre de la Computadora: ")
        print("Datos del Monitor....")
        marca_monitor = input("Ingrese la marca del monitor: ")
        tamanio = input("Ingrese el Tamaño en pulgadas del monitor: ")
        monitor1 =  Monitor(marca_monitor, tamanio)
        print("Datos del Teclado...")
        marca_teclado = input("Ingrese marca del teclado: ")
        tipo_teclado = input("Ingrese el tipo de entrada del teclado: ")
        teclado1 = Teclado(marca_teclado, tipo_teclado)
        print("Datos del Mouse...")
        marca_raton = input("Ingrese marca del moouse: ")
        tipo_raton = input("Ingrese la entrada del mouse: ")
        raton1 = Raton(marca_raton, tipo_raton)
        compu1 = Computadora(nombre, monitor1, teclado1, raton1)
        ordenes.append(compu1)
        print("Computadora Agregada a la orden")
        print()
        seguir = input("Para terminar con la orden ingrese (FIN): ")
        if seguir == "FIN" or seguir == "fin":
            break
    orden1 = Orden(ordenes)
    print(orden1)
    print()
    otra_orden = input("Quiere agreagar otra orden? (Y/N)")
    if otra_orden == "Y" or otra_orden == "y":
        continue
    elif otra_orden == "N" or otra_orden == "n":
        break
