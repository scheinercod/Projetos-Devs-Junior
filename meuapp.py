from cgitb import text
import tkinter as tk
from tkinter.ttk import Button

cor1 = "#040608" #preto

def cmd_Click():
    print("oi")

root = tk.Tk()
root.title("Aplicativos Populares")
root.geometry("400x240")
root.iconbitmap('imgs/oculos.ico')
root.config(bg=cor1)

cmd = Button(text="Executar", command=cmd_Click)
cmd.pack()


    

root.mainloop()
