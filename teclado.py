from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, marca, tipo):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo)
    
    def __str__(self):
        return "Teclado: id: {}, marca: {}, tipo de entrada: {}".format(self.__id_teclado, self._marca, self._tipo_entrada)
    

