class Transicion:
    def __init__(self, inicio, final, transicion):
        self.inicio = inicio
        self.final = final
        self.transicion = transicion

    def getInicio(self):
        return self.inicio

    def getFinal(self):
        return self.final

    def getTransicion(self):
        return self.transicion

    def setInicio(self, inicio):
        self.inicio = inicio

    def setFinal(self, destino):
        self.destino = destino

    def setTransicion(self, transicion):
        self.transicion = transicion