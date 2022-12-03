class Estado:
    def __init__(self, estado):
        self.estado = estado
        self.listaAdyacentes = []

    def getEstado(self):
        return self.estado

    def setEstado(self, estado) -> None:
        self.estado = estado

    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self, listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes