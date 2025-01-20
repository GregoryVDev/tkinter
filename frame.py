# Organiser l'espace à l'aide des frames en tkinter
from tkinter import *

master = Tk()
master.title("Exemple de mise en page Tkinter")
master.geometry("1300x800+50+50")

# Permet d'ajouter un background
frame_top = Frame(master, bg= "#1a8cff")
# Permet de positionner le frame
frame_top.place(x=0, y=0, width=1300, height=200)


# Permet d'ajouter un background
frame_left = Frame(master, bg="#ff8000")
# Permet de positionner le frame
frame_left.place(x=0, y=200, width=200, height=500)


# Permet d'ajouter un background
frame_right = Frame(master, bg="#9dc8e3")
# Permet de positionner le frame
frame_right.place(x=200, y=200, width=1100, height=500)


# Permet d'ajouter un background
frame_bottom = Frame(master, bg="#154e72")
# Permet de positionner le frame
frame_bottom.place(x=000, y=700, width=1300, height=100)

# Permet d'ouvrir la page
master.mainloop()
