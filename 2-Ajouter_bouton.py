#https://www.youtube.com/watch?v=N4M4W7JPOL4

from tkinter import *

window = Tk()
window.title("My App")
window.geometry ("1080x720")
window.minsize(480, 360)
window.config(background='#89B3F9')

frame= Frame(window, bg="#89B3F9", bd=1, relief=SUNKEN)

label_title=Label(frame, text="Tuto pour", font=("Helvetica", 50), bg='red', fg='yellow')
label_title.pack()

label_subtitle=Label(frame, text="TKinter", font=("Helvetica", 30), bg='red', fg='yellow')
label_subtitle.pack()

#Creer un bouton
gihub_button= Button(frame, text="Ouvrir GitHub",font=("Helvetica", 30), bg='yellow', fg='red')
#gihub_button=le nom du bouton #frame=lendroit ou on place le bouton #
gihub_button.pack(pady=25, fill=X)
#pady=.. place laisser entre texte et bouton #Pour que le bouton prenne toute la largeur

frame.pack(expand=YES)

window.mainloop()
