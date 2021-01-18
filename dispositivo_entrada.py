class DispositivoEntrada:
    def __init__(self, marca, tipo):
        self._marca = marca
        self._tipo_entrada = tipo

    
    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca

    def get_tipo_entrada(self):
        return self._tipo_entrada
    def set_tipo_entrada(self, tipo):
        self._tipo_entrada = tipo
    


