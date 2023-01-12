from tkinter import *
from store import store
from views.theme import THEME


class Topbar(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent, bg=THEME['blueTopbar'], height=150)

    def getSignUpLink(self) -> None:
        store.getApp().setCurrentFrame('signup')

    def getSignInLink(self) -> None:
        store.getApp().setCurrentFrame('signin')

    def pack(self) -> None:
        super().pack(side="top", fill="x")
        title = Label(self, font=('aria', 30, 'bold'),
                      text="Quizz", fg="steel blue", bd=10, anchor='w')
        title.pack(side="left")

        buttonContainer = Frame(
            self, bg="#7FB8ED", borderwidth=0, height=450, width=855)
        buttonContainer.pack(side='right')

        signUpLink = self.getSignUpLink
        signUpBtn = Button(buttonContainer, text='Sign Up', bg='#31468F',
                           fg='white', activebackground='#052B71',  font=('Inter', 40), command=signUpLink)
        signUpBtn.pack(side="left")

        signInLink = self.getSignInLink
        signInBtn = Button(buttonContainer, text='Sign In', bg='#31468F',
                           fg='white', activebackground='#052B71',  font=('Inter', 40), command=signInLink)
        signInBtn.pack(side='right')
