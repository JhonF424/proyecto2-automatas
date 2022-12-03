from Estados.Estado import *
from Transiciones.Transicion import *

class Automata:
    def __init__(self) -> None:
        self.listaEstados = []
        self.listaTransiciones = []
    
    
    def ingresarEstado(self, dato):
        if not self.verificarExisteE(dato):
            self.listaEstados.append(Estado(dato))

            
    def verificarExisteE(self, dato):
        for i in self.listaEstados:
            if dato == i.getEstado():
                return True
        return False

        
        
    def ingresarTransicion(self, origen, destino, trans):
        if not self.verificarListaT(origen, destino):
            if self.verificarExisteE(origen) and self.verificarExisteE(destino):
                self.listaTransiciones.append(Transicion(origen, destino, trans))
                self.obtenerEstado(origen).getListaAdyacentes().append(destino)

    """ verifica que el origen y destino que entran no se encuentren en ese orden en alguna arista """

    def verificarListaT(self, origen, destino):
        for i in self.listaTransiciones:
            if origen == i.getOrigen() and destino == i.getDestino():
                return True
        return False

    """como el metodo menciona obtiene el vertice buscado de la lista de vertices del grafo"""
    def obtenerEstado(self, dato):
        for i in self.listaEstados:
            if dato == i.getDato():
                return i