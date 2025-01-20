# Amélioration des grilles et des widgets
from tkinter import *

window = Tk()
window.title("Exploration des grilles en Tkinter")
# Mettre des dimensions pour la fenêtre. On ajoute +200 pour l'espace en px qui va séparer la fenêtre du bord gauche de l'écran. On ajoute +150 pour la distance qui va séparer notre fenêtre du bord supérieur de l'écran
window.geometry("900x600+200+150")

def validate():
    # Afficher un message avec le nom et le prénom
    message = "Vous êtes : "+text_name.get()+ " "+text_firstname.get()
    # Quand on appuie sur "valider" on affiche la variable "message"
    labelMessage.config(text=message)

def reset():
    # Affiche aucun text
    labelMessage.config(text="")
    # Quand je clique sur réinisialiser, je veux que le text soit vide
    text_name.delete(0,END)
    text_firstname.delete(0,END)

# Ecrire un text dans la fenêtre (bd = bordure)
label_firstname = Label(window, text="Votre prénom", bd=2, font=("Arial", 15, "bold"), fg= "red")
# Afficher dans un grid (1 ligne, 1 colonne, en position sticky vers l'est avec un padding extérieur de 20px
label_firstname.grid(row=1, column=1, sticky = "E", padx = 20, pady=15)


label_name = Label(window, text="Votre nom", bd=2, font=("Arial", 15, "bold"), fg= "red")
label_name.grid(row=2,column=1, sticky = "E", padx = 20, pady=15)

# Ajoute un input à côté du text "Votre prénom"
text_firstname = Entry(window)
text_firstname.grid(row=1, column=2)

text_name = Entry(window)
text_name.grid(row=2, column=2)

# Créer le bouton "valider"
submit = Button(window, text="Valider", font=("Times new roman", 14), command=validate)
submit.grid(row=3, column=1)

# Créer le bouton "réinisialiser"
reset = Button(window, text="Réinisialiser", font=("Times new roman", 14), command=reset)
reset.grid(row=3, column=2)

# Créer le bouton "quitter"
leave = Button(window, text="Quitter", font=("Times new roman", 14), command=window.quit)
leave.grid(row=3, column=3)

# Permet d'afficher le text quand on a appuyé sur valider
labelMessage = Label(window, text="", font=("Times new roman", 14), fg="blue")
# Le message prend de la colonne 1 à 3
labelMessage.grid(row = 5, column = 1, columnspan = 2, padx = 20)



window.mainloop()