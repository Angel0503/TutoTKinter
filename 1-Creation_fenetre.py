#https://www.youtube.com/watch?v=N4M4W7JPOL4

#Importer 'tkinter'
from tkinter import *
#Creer une premiere fenetre
window = Tk()

#Personnaliser fenetre

window.title("My App")                         #Titre fenetre

window.geometry ("1080x720")                   #Taille fenetre

window.minsize(480, 360)                       #Taille min fenetre

#window.iconbitmap("quelque chose.ico") pour changer l'icone de la fenetre

window.config(background='#89B3F9')            #Changer la couleur du fond

#Creer la frame(une hitbox ou les textes seront mit dedans)
frame= Frame(window, bg="#89B3F9", bd=1, relief=SUNKEN)
#Maj frame obligatoire #bg=couleur frame #bd=bordure #relief=SUNKEN pour quil y est un relief

#Ajouter un premier texte
label_title=Label(frame, text="Bienvenue", font=("Helvetica", 50), bg='red', fg='yellow')
#Maj label obligatoire #le frame est fait pour dire quon met le texte dans frame #le font=(".....") sert a changer la police d'ecriture #Puis on choisi la taille #On choisi la couleur du background #On choisi la couleur du texte

#label_title.pack(side="left")
#Pour afficher le texte #side="..." pour choisir lemplacement du texte
#OU
label_title.pack()#(expand=YES)
#Pour que le texte soir toujours au milieu meme si on change la taille de la fenetre

#Ajouter un second texte
label_subtitle=Label(frame, text="Ca va?", font=("Helvetica", 30), bg='red', fg='yellow')
label_subtitle.pack()

#Ajouter la frame
frame.pack(expand=YES)

#Afficher la fenetre
window.mainloop()


