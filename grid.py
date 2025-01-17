# Les grilles et les champs de texte
from tkinter import *

window = Tk()
window.title("Exploration des grilles en Tkinter")
window.geometry()
label_name = Label(window, text="Votre prénom")
label_name.grid(row=1, column=1, sticky = "E", padx = 20)

window.mainloop()