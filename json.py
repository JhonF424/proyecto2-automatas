import json
# from clases.Grafo import *


class ManejoJson:

    def cargar_estados(self, automata):
        with open('data/verticesP.json') as contenido:
            estados = json.load(contenido)
            for estado in estados:
                automata.ingresarEstado(estado.get("estado"))

    def cargar_transiciones(self, automata):
        with open('data/transiciones.json') as contenido:
            transiciones = json.load(contenido)
            for transicion in transiciones:
                automata.ingresarTransicion(transicion.get("origen"), transicion.get(
                    "destino"), transicion.get("trans"))
