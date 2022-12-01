from Estados.Estado import *


class Transicion:
    def __init__(self, origen: Estado, destino: Estado, trans: int):
        self.origen = origen
        self.destino = destino
        self.trans = trans

    def get_origen(self) -> Estado:
        return self.origen

    def get_destino(self) -> Estado:
        return self.destino

    def get_trans(self) -> int:
        return self.trans
