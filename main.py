import tkinter as tk
from Automata import *
from ControlJson import *
CJ = ControlJson()
At1 = Automata()
At2 = Automata()
At3 = Automata()
Union = Automata()
# Interseccion = Automata()
CJ.crearNodosA(At1)
CJ.crearNodosB(At2)
CJ.crearNodosAFND(At3)
CJ.crearTransicionA(At1)
CJ.crearTransicionB(At2)
CJ.crearTransicionAFND(At3)
# Union.Union(At1.getListaNodos(),At2.getListaNodos(),At1.getListaTransi(),At2.getListaTransi())
# Interseccion.Interseccion(At1.getListaNodos(),At2.getListaNodos())
window = tk.Tk()
window.geometry("800x600")

# Autómata 1
lat1 = tk.Label(window, text="Autómata 1", font="verdana")
bat1 = tk.Button(window, text="Mostrar autómata", width=15, height=2, font="verdana", command=At1.automata)
lat1.place(relx=0.17, rely=0.0, anchor='ne')
bat1.place(relx=0.21, rely=0.08, anchor='ne')
bat2 = tk.Button(window, text="Reverso", width=15, height=2, font="verdana", command=At1.reverso)
bat2.place(relx=0.21, rely=0.20, anchor='ne')
bat3 = tk.Button(window, text="Complemento", width=15, height=2, font="verdana", command=At1.complemento)
bat3.place(relx=0.21, rely=0.31, anchor='ne')

# Autómata 2
lat1 = tk.Label(window, text="Autómata 2", font="verdana")
bat1 = tk.Button(window, text="Mostrar autómata", width=15, height=2, font="verdana", command=At2.automata)
lat1.place(relx=0.42, rely=0.0, anchor='ne')
bat1.place(relx=0.45, rely=0.08, anchor='ne')
bat2 = tk.Button(window, text="Reverso", width=15, height=2, font="verdana", command=At2.reverso)
bat2.place(relx=0.45, rely=0.20, anchor='ne')
bat3 = tk.Button(window, text="Complemento", width=15, height=2, font="verdana", command=At2.complemento)
bat3.place(relx=0.45, rely=0.31, anchor='ne')

# Autómata 3
lat1 = tk.Label(window, text="Autómata 3", font="verdana")
bat1 = tk.Button(window, text="Mostrar autómata", width=15, height=2, font="verdana", command=At3.automata)
lat1.place(relx=0.17, rely=0.45, anchor='ne')
bat1.place(relx=0.21, rely=0.5, anchor='ne')
bat2 = tk.Button(window, text="Convertir a AFD", width=15, height=2, font="verdana", command=At3.svat)
bat2.place(relx=0.21, rely=0.61, anchor='ne')
# bat3 = tk.Button(window, text="Complemento", width=15, height=2, font="verdana", command=At2.complemento)
# bat3.place(relx=0.45, rely=0.31, anchor='ne')

# Operaciones
lop1 = tk.Label(window, text="Operaciones entre autómatas", font="verdana")
bop1 = tk.Button(window, text="Unión", width=15, height=2, font="verdana", command=At1.ru)
lop1.place(relx=0.89, rely=0.0, anchor="ne")
bop1.place(relx=0.85, rely=0.08, anchor='ne')
bop2 = tk.Button(window, text="Intersección", width=15, height=2, font="verdana", command=At1.rr)
bop2.place(relx=0.85, rely=0.20, anchor='ne')
window.mainloop()


