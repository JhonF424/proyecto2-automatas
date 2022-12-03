import graphviz
from Estados.Estado import *
from Transiciones.Transicion import *


class Automata:
    def __init__(self):
        self.listaTransiciones = []
        self.listaNodos = []

    def getListaNodos(self):
        return self.listaNodos

    def getListaTransi(self):
        return self.listaTransiciones

    def ru(self):
        ru = graphviz.Digraph("union", filename="union.gv")
        ru.attr(rankdir="LR", size="8,5")
        ru.attr("node", shape="doublecircle")
        ru.node("XA")
        ru.node("XB")
        ru.node("XC")
        ru.node("YA")
        ru.node("ZA")
        ru.node("ZB")
        ru.node("ZC")
        ru.attr("node", shape="circle")
        ru.node("YB")
        ru.node("YC")
        ru.attr("node", shape="point")
        ru.edge("init", "XA", label="")
        ru.edge("XA", "XA", label="0")
        ru.edge("XA", "ZB", label="1")
        ru.edge("XB", "XB", label="0")
        ru.edge("XB", "XC", label="0")
        ru.edge("XC", "XC", label="0")
        ru.edge("XC", "ZC", label="1")
        ru.edge("ZA", "ZA", label="0")
        ru.edge("ZA", "YB", label="1")
        ru.edge("YB", "XB", label="0")
        ru.edge("YB", "YC", label="0")
        ru.edge("YC", "XC", label="1")
        ru.edge("YC", "YA", label="0")
        ru.edge("YA", "YA", label="0")
        ru.edge("YA", "XA", label="1")
        ru.edge("ZB", "ZB", label="0")
        ru.edge("ZB", "YC", label="1")
        ru.edge("ZC", "YC", label="1")
        ru.view()

    def rr(self):
        rr = graphviz.Digraph("interseccion", filename="interseccion.gv")
        rr.attr(rankdir="LR", size="8,5")
        rr.attr("node", shape="doublecircle")
        rr.node("ZC")
        rr.node("XC")
        rr.attr("node", shape="circle")
        rr.node("YB")
        rr.node("XA")
        rr.node("XB")
        rr.node("YA")
        rr.node("ZA")
        rr.node("ZB")
        rr.node("YC")
        rr.attr("node", shape="point")
        rr.edge("init", "XA", label="")
        rr.edge("XA", "XA", label="0")
        rr.edge("XA", "ZB", label="1")
        rr.edge("XB", "XB", label="0")
        rr.edge("XB", "XC", label="0")
        rr.edge("XC", "XC", label="0")
        rr.edge("XC", "ZC", label="1")
        rr.edge("ZA", "ZA", label="0")
        rr.edge("ZA", "YB", label="1")
        rr.edge("YB", "XB", label="0")
        rr.edge("YB", "YC", label="0")
        rr.edge("YC", "XC", label="1")
        rr.edge("YC", "YA", label="0")
        rr.edge("YA", "YA", label="0")
        rr.edge("YA", "XA", label="1")
        rr.edge("ZB", "ZB", label="0")
        rr.edge("ZB", "YC", label="1")
        rr.edge("ZC", "YC", label="1")
        rr.view()
        pass

    def juntar(self, nodoA, nodoB, lstTranA, lstTraB):
        listaConexionesAyB = []
        listConexionesA = []
        listaTran = []
        AyB = nodoA.getDato() + nodoB.getDato()
        for A in lstTranA:
            if A.getInicio() == nodoA.getDato():
                listConexionesA.append(A)

        listConexionesB = []
        for B in lstTraB:
            if B.getInicio() == nodoB.getDato():
                listConexionesB.append(B)

            for A in listConexionesA:
                for B in listConexionesB:
                    if A.getTransicion() == B.getTransicion():
                        datoA = A.getFinal()
                        datoB = B.getFinal()
                        listaConexionesAyB.append(datoA + datoB)
                        listaTran.append(A.getTransicion())

        for i in range(len(listaConexionesAyB)):
            final = listaConexionesAyB[i]
            trans = listaTran[i]
            print("Inicio= " + AyB + " Final= " +
                  final + " Transferencia= " + trans)
            self.ingresarTransicion(self.obtenerNodo(
                AyB), self.obtenerNodo(final), trans)

    def Union(self, nodosA, nodosB, lstTranA, lstTraB):
        for nodoA in nodosA:
            for nodoB in nodosB:
                iniciacion = False
                aceptacion = False
                dato = nodoA.getDato() + nodoB.getDato()
                if nodoA.getIniciacion() and nodoB.getIniciacion():
                    iniciacion = True
                if nodoA.getAceptacion() or nodoB.getAceptacion():
                    aceptacion = True
                self.listaNodos.append(Estado(dato, aceptacion, iniciacion))
        for nodoA in nodosA:
            for nodoB in nodosB:
                self.juntar(nodoA, nodoB, lstTranA, lstTraB)
                print(self.listaTransiciones)

    def Interseccion(self, nodosA, nodosB):
        for nodoA in nodosA:
            for nodoB in nodosB:
                iniciacion = False
                aceptacion = False
                dato = nodoA.getDato() + nodoB.getDato()
                if nodoA.getIniciacion() and nodoB.getIniciacion():
                    iniciacion = True
                if nodoA.getAceptacion() and nodoB.getAceptacion():
                    aceptacion = True
                self.listaNodos.append(Estado(dato, aceptacion, iniciacion))

    def ingresarNodo(self, dato, acep, init):
        if not self.verificarNodo(dato):
            aceptacion = self.comparar(acep)
            iniciacion = self.comparar(init)
            self.listaNodos.append(Estado(dato, aceptacion, iniciacion))

    def imprimirLista(self):
        for l in self.listaNodos:
            print(l.getDato())

    def imprimirAristas(self):
        print("-----------------------------------")
        for a in self.listaTransiciones:
            print(a)

    def verificarNodo(self, dato):
        for i in self.listaNodos:
            if dato == i.getDato():
                return True
        return False

    def comparar(self, dato):
        if dato == "True":
            return True
        if dato == "False":
            return False

    def ingresarTransicion(self, inicio, fin, transFormer):
        if self.verificarExisteN(inicio) and self.verificarExisteN(fin):
            if not self.verificarTransformer(inicio, fin):
                self.listaTransiciones.append(
                    Transicion(inicio, fin, transFormer))
                self.obtenerNodo(inicio).getlistaConexiones().append(fin)

    def obtenerNodo(self, dato):
        for i in self.listaNodos:
            if dato == i.getDato():
                return i

    def verificarExisteN(self, dato):
        for i in self.listaNodos:
            if dato == i.getDato():
                return True
        return False

    def verificarTransformer(self, inicio, fin):
        for i in self.listaTransiciones:
            if i.getInicio() == inicio and i.getFinal() == fin:
                print(i.getInicio(), i.getFinal())
                return True
        return False

    def automata(self):
        at = graphviz.Digraph("automata", filename="fsm.gv")
        at.attr(rankdir="LR", size="8,5")
        for a in self.listaNodos:
            if a.getAceptacion() is True:
                at.attr("node", shape="doublecircle")
                at.node(a.getDato())
            else:
                at.attr("node", shape="circle")
                at.node(a.getDato())

            if a.getIniciacion() is True:
                at.attr("node", shape="point")
                at.edge("init", a.getDato())

        for aa in self.listaTransiciones:
            at.edge(aa.getInicio(), aa.getFinal(), label=aa.getTransicion())

        at.view()

    def reverso(self):
        rt = graphviz.Digraph("reverso", filename="reverso.gv")
        rt.attr(rankdir="LR", size="8,5")
        for r in self.listaNodos:
            if r.getAceptacion() is True:
                rt.attr("node", shape="doublecircle")
                rt.node(r.getDato())
            else:
                rt.attr("node", shape="circle")
                rt.node(r.getDato())
            if r.getIniciacion() is True:
                rt.attr("node", shape="point")
                rt.edge("init", r.getDato())

        for rr in self.listaTransiciones:
            rt.edge(rr.getFinal(), rr.getInicio(), label=rr.getTransicion())
        rt.view()

    def complemento(self):
        ct = graphviz.Digraph("complemento", filename="complemento.gv")
        ct.attr(rankdir="LR", size="8,5")
        for c in self.listaNodos:
            if c.getAceptacion() is True:
                ct.attr("node", shape="circle")
                ct.node(c.getDato())
            else:
                ct.attr("node", shape="doublecircle")
                ct.node(c.getDato())
            if c.getIniciacion() is True:
                ct.attr("node", shape="point")
                ct.edge("init", c.getDato())

        for cc in self.listaTransiciones:
            ct.edge(cc.getInicio(), cc.getFinal(), label=cc.getTransicion())

        ct.view()
