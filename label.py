# Création des fenêtres et des labels
from tkinter import *
window = Tk()
window.geometry("1200x800")
# Ecrire dans la fenêtre "Bonjour" sans que ça s'affiche
label1 = Label(window, text="Bonjour")
# Afficher l'écriture dans la fenêtre
label1.pack()

window.mainloop()