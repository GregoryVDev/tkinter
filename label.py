# Les grilles en tkinter
from tkinter import *
window = Tk()
window.geometry("1200x800")
# Ecrire dans la fenêtre "Bonjour" sans que ça s'affiche
label1 = Label(window, text="Bonjour")
# Afficher le text dans la fenêtre
label1.pack()

# Créer un bouton afin de pouvoir quitter la fenêtre
button_leave = Button(window, text="Quitter", command=window.quit, width = 30, height=10)
# Afficher le bouton quitter dans la fenêtre (mettre un slide pour mettre le bouton à gauche de la fenêtre), un padding extérieur (padx) et un padding intérieur (ipadx)
button_leave.pack(side=LEFT, padx = 300, ipadx = 400)

window.mainloop()
