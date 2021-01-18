from computadora import Computadora

class Orden:
    contador_orden = 0
    
    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.__id_orden = Orden.contador_orden
        self.__computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora)
    
    def __str__(self):
        TempCom = ""
        for compu in self.__computadoras:
            TempCom += compu.__str__()
        return f"Orden: {self.__id_orden}, Computadoras:\n\t{TempCom}"

