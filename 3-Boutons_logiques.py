#https://www.youtube.com/watch?v=N4M4W7JPOL4

from tkinter import *
#Nouvel import
import webbrowser #sert a ouvrir des pages internet

def open_link():
    webbrowser.open_new("https://github.com/Angel0503")
#def est la fonction du nom de notre bouton #mettre l'url dans webbrowser...

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

gihub_button= Button(frame, text="Ouvrir GitHub",font=("Helvetica", 30), bg='yellow', fg='red', command=open_link)
gihub_button.pack(pady=25, fill=X)                                                              #command+fonction du bouton

frame.pack(expand=YES)

window.mainloop()
