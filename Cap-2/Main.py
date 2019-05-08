import tkinter
from tkinter import messagebox
from tkinter import ttk
import FDTD
import ShowPlt
import Materiais
import time

tk = tkinter.Tk()
tk.wm_maxsize(width=500,height=500)
tk.wm_minsize(width=450,height=450)
tk.title("FDTD Program")
value = tkinter.IntVar()

def selection():
    global raioE

    if(value.get() == 2):
        raioE.config(state='normal')
    else:
        raioE.config(state='disabled')
        

FDTD1 = tkinter.Radiobutton(tk,text="FDTD 1-Dimension", variable = value, value = 1, command = selection)
FDTD2 = tkinter.Radiobutton(tk,text="FDTD 2-Dimension", variable = value, value = 2, command = selection)
FDTD3 = tkinter.Radiobutton(tk,text="FDTD 3-Dimension", variable = value, value = 3, command = selection)
FDTD1.pack()
FDTD2.pack()
FDTD3.pack()
L1 = tkinter.Label(tk, text="Cells: ")
L1.pack()
E1 = tkinter.Entry(tk, width=10)
E1.pack()

L4 = tkinter.Label(tk, text="Steps: ")
L4.pack()
E4 = tkinter.Entry(tk, width=10)
E4.pack()


L2 = tkinter.Label(tk, text="ε: ", font=10)
L2.pack()
E2 = tkinter.Entry(tk, width=10)
E2.pack()

L3 = tkinter.Label(tk, text="σ: ", font=10)
L3.pack()
E3 = tkinter.Entry(tk, width=10)
E3.pack()

raio = tkinter.Label(tk, text="Radius: ", font=10)
raio.pack()
raioE = tkinter.Entry(tk, width=10, state='disabled')
raioE.pack()


def funcao():
    graph = ShowPlt.showPlt(1,-1)
    global value, E1, E2, E3, raioE
    if(value.get() == 1):
        if(E1.get() != "" and E4.get() != "" and E1.getint(E1.get()) > 0 and E4.getint(E4.get())):
            if(E2.get() != "" and E3.get() != "" and E2.getdouble(E2.get()) >= 0 and E3.getdouble(E3.get()) >= 0):
                material = Materiais.DielCond(E1.getint(E1.get())//2, E2.getdouble(E2.get()), E1.getint(E1.get()), E3.getdouble(E3.get()))
                material.init()
                fdtd = FDTD.FDTD(graph, E1.getint(E1.get()), E4.getint(E4.get()) , material)
                fdtd.init()
                fdtd.loopFDTD()
                
            else:
                messagebox.showinfo("Error","Fill all parameters")
        else:
            messagebox.showinfo("Error","Fill all parameters")
    elif(value.get() == 2):
        if(E1.get() != "" and E1.getint(E1.get()) > 0):
            if(E2.get() != "" and E3.get() != "" and E2.getdouble(E2.get()) > 0 and E3.getdouble(E3.get()) > 0):
                cilindro = Materiais.Cilinder(raioE.getint(raioE.get()), E4.getint(E4.get()),E3.getdouble(E3.get()) , E1.getint(E1.get())//2,E1.getint(E1.get())//2, E1.getint(E1.get()))
                cilindro.init()
                fdtd = FDTD.FDTD2D(cilindro, graph, E4.getint(E4.get()) , 0, E1.getint(E1.get()), E1.getint(E1.get()))
                fdtd.init(20)
                fdtd.loopFDTD()
            else:
                messagebox.showinfo("Error","Fill all parameters")
    elif(value.get() == 3):
        messagebox.showinfo("FDTD 3-D","FDTD 3-dimensions is coming ")
    else:
        messagebox.showinfo("Error","Fill all parameters")

button = tkinter.Button(tk,text = "start", command = funcao)
button.pack()
label = tkinter.Label(tk)
label.pack()
tk.mainloop()

'''
from Materiais import DielCond
import FDTD
import ShowPlt
d = DielCond(100, 3, 500,1)
sh = ShowPlt.showPlt(1,-1)

d.init()

method = FDTD.FDTD(sh, 500, 200,d)

method.init()
method.loopFDTDFourier()
'''
'''
from Materiais import Cilinder
from FDTD import FDTD2D
import ShowPlt

cilindro = Cilinder(20, 0.1,50 , 15, 150, 150)

sh = ShowPlt.showPlt(1,-1)

cilindro.init()

method = FDTD2D(cilindro,sh,200,300,150,150)
method.init(20)
method.loopFDTD()
'''
'''
from Materiais import Cilinder
from FDTD import FDTD2D
import ShowPlt

cilindro = Cilinder(1, 0.1,50 , 25,25 , 50)
#cilindro2 = Cilinder(4,0.1,50, 20,20,50)
sh = ShowPlt.showPlt(1,-1)

cilindro.init()
#cilindro2.init()
method = FDTD2D(cilindro,sh,150,0,50,50)
method.init(20)
method.loopFDTD()

'''