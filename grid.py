# Les grilles et les champs de text
from tkinter import *

window = Tk()
window.title("Exploration des grilles en Tkinter")
# Mettre des dimensions pour la fenêtre
window.geometry("600x400")

def validate():
    pass

def reset():
    pass


# Ecrire un text dans la fenêtre
label_firstname = Label(window, text="Votre prénom")
# Afficher dans un grid (1 ligne, 1 colonne, en position sticky vers l'est avec un padding extérieur de 20px
label_firstname.grid(row=1, column=1, sticky = "E", padx = 20)


label_name = Label(window, text="Votre nom")
label_name.grid(row=2,column=1, sticky = "E", padx = 20)

# Ajoute un input à côté du text "Votre prénom"
text_firstname = Entry(window)
text_firstname.grid(row=1, column=2)

text_name = Entry(window)
text_name.grid(row=2, column=2)

# Créer le bouton "valider"
submit = Button(window, text="Valider", command=validate)
submit.grid(row=3, column=1)

# Créer le bouton "réinisialiser"
reset = Button(window, text="Réinisialiser", command=reset)
reset.grid(row=3, column=2)

# Créer le bouton "quitter"
leave = Button(window, text="Quitter", command=window.quit)
leave.grid(row=3, column=3)

window.mainloop()