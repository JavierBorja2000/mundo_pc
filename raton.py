from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        super().__init__(marca, tipo)

    def __str__(self):
        return "Raton: id: {}, Marca: {}, Tipo de Entrada: {}".format(self.__id_raton, self._marca, self._tipo_entrada)

