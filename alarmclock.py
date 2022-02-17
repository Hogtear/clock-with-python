from cProfile import label
from tkinter import *
from tkinter.ttk import *

from time import strftime

# Cabeçalho do Programa
root = Tk()
root.title("Relógio")

# Função do tempo
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

# Customização do Relógio
label = Label(root, font=("ds-digital", 80), background="black", foreground="green")
label.pack(anchor="center")
time()

# Loop necessário para o Funcionamento
mainloop()