# Comment placer les widgets dans les frames
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


label_top = Label(frame_top, text="Texte label haut", width=30, height=3)
label_top.grid(row=0, column=1, padx=20, pady=20)


label_top2 = Label(frame_top, text="Texte label haut", width=30, height=3)
label_top2.grid(row=1, column=1, padx=20, pady=20)


label_left = Label(frame_left, text="Texte label gauche", width=15, height=3)
label_left.grid(row=0, column=1, padx=20, pady=20)


label_right = Label(frame_right, text="Texte label gauche", width=30, height=3)
label_right.grid(row=0, column=1, padx=20, pady=20)



# Permet d'ouvrir la page
master.mainloop()
