from tkinter import *
from views.theme import THEME
# from pathlib import Path


class Topbar(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent, bg=THEME['blueTopbar'], height=150)

    def pack(self) -> None:
        super().pack(side="top", fill="x")
        title = Label(self, font=('aria', 30, 'bold'),
                      text="Quizz", fg="steel blue", bd=10, anchor='w')
        title.pack(side="left")

        buttonContainer = Frame(
            self, bg="#7FB8ED", borderwidth=0, height=450, width=855)
        buttonContainer.pack(side='right')

        signUpBtn = Button(buttonContainer, text='Sign Up', bg='#31468F',
                           fg='white', activebackground='#052B71',  font=('Inter', 40))
        signUpBtn.pack(side="left")

        signInBtn = Button(buttonContainer, text='Sign In', bg='#31468F',
                           fg='white', activebackground='#052B71',  font=('Inter', 40))
        signInBtn.pack(side='right')
