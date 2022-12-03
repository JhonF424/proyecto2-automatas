class Estado:
    def __init__(self, dato, aceptacion, iniciacion):
        self.dato = dato
        self.aceptacion = aceptacion
        self.iniciacion = iniciacion
        self.listaConexiones = []

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getAceptacion(self):
        return self.aceptacion

    def setAceptacio(self, aceptacion):
        self.aceptacion = aceptacion

    def getIniciacion(self):
        return self.iniciacion

    def setAceptacion(self, iniciacion):
        self.iniciacion = iniciacion

    def getlistaConexiones(self):
        return self.listaConexiones
