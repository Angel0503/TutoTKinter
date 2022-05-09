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
window.config(background='#89B3F9')            #Changer la couleur du fond(code hexadecimal des couleurs)

#Afficher la fenetre
window.mainloop()


