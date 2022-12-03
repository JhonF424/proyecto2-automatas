from Estados.Estado import *


class Transicion:
    def __init__(self, origen: Estado, destino: Estado, trans: int):
        self.origen = origen
        self.destino = destino
        self.trans = trans

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getTrans(self):
        return self.trans

    def setOrigen(self, origen):
        self.origen = origen

    def setDestino(self, destino):
        self.destino = destino

    def setTrasn(self, trans):
        self.trans = trans
