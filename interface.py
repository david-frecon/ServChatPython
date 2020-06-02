from tkinter import *

fen = Tk()
fen.geometry("800x800")
T = Text(fen)
T.pack()
button = Button(fen,text = "quitter", command = fen.quit).pack()

print(T)
for i in range (5):
    T.insert(END,str(i)+"\n")

mainloop()

"""
import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()"""