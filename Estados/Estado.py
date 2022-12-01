class Estado:
    def __init__(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_estado(self, estado) -> None:
        self.estado = estado
