import json


class ControlJson:

    def crearNodosA(self, Automata):
        with open('data/nodos.json') as contenido:
            nodos = json.load(contenido)
            for nodo in nodos:
                Automata.ingresarNodo(nodo.get("estado"), nodo.get(
                    "aceptacion"), nodo.get("iniciacion"))

    def crearNodosB(self, Automata):
        with open('data/nodos2.json') as contenido:
            nodos = json.load(contenido)
            for nodo in nodos:
                Automata.ingresarNodo(nodo.get("estado"), nodo.get(
                    "aceptacion"), nodo.get("iniciacion"))

    def crearTransicionA(self, Automata):
        with open('data/transiciones.json') as contenido:
            transiciones = json.load(contenido)
            for trans in transiciones:
                Automata.ingresarTransicion(
                    trans.get("inicio"), trans.get("final"), trans.get("transicion"))

    def crearTransicionB(self, Automata):
        with open('data/transiciones2.json') as contenido:
            transiciones = json.load(contenido)
            for trans in transiciones:
                Automata.ingresarTransicion(
                    trans.get("inicio"), trans.get("final"), trans.get("transicion"))

    def crearNodosAFND(self, Automata):
        with open('data/nodos3.json') as contenido:
            nodos = json.load(contenido)
            for nodo in nodos:
                Automata.ingresarNodo(nodo.get("estado"), nodo.get(
                    "aceptacion"), nodo.get("iniciacion"))

    def crearTransicionAFND(self, Automata):
        with open('data/transiciones3.json') as contenido:
            transiciones = json.load(contenido)
            for trans in transiciones:
                Automata.ingresarTransicion(
                    trans.get("inicio"), trans.get("final"), trans.get("transicion"))