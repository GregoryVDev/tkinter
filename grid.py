# Les grilles et les commandes de boutons
from tkinter import *

window = Tk()
window.title("Exploration des grilles en Tkinter")
# Mettre des dimensions pour la fenêtre
window.geometry("600x400")

def validate():
    # Afficher un message avec le nom et le prénom
    message = "Vous êtes : "+text_name.get()+ " "+text_firstname.get()
    # Quand on appuie sur "valider" on affiche la variable "message"
    labelMessage.config(text=message)

def reset():
    # Quand je clique sur réinisialiser, je veux que le text soit vide
    text_name.delete(0,END)
    text_firstname.delete(0,END)
    # Affiche aucun text
    labelMessage.config(text="")


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

# Permet d'afficher le text quand on a appuyé sur valider
labelMessage = Label(window, text="")
# Le message prend de la colonne 1 à 3
labelMessage.grid(row = 5, column = 1, columnspan = 3, padx = 20)



window.mainloop()