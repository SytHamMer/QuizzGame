from tkinter import *
from dbHandler import createQuizz
from store import store
from views.theme import THEME


class Topbar(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent, bg=THEME['blueTopbar'], height=150)

    def getHomeLink(self) -> None:
        store.getApp().setCurrentFrame('home')

    def getSignUpLink(self) -> None:
        store.getApp().setCurrentFrame('signup')

    def getSignInLink(self) -> None:
        store.getApp().setCurrentFrame('signin')

    def deconnect(self) -> None:
        store.setUser(None)
        store.getApp().setCurrentFrame('home')
    def createQuizzLink(self):
        store.getApp().setCurrentFrame('creation')

    def pack(self) -> None:
        super().pack(side="top", fill="x")

        homeLink = self.getHomeLink
        title = Button(self, font=('aria', 30, 'bold'),
                       text="Quizz", fg="steel blue", bd=0, anchor='w', command=homeLink)
        title.pack(side="left", padx=20, pady=20)

        username = store.getUser()
        userIsLogged = username != None

        if (userIsLogged):
            userLabel = Label(self, font=('aria', 30, 'bold'),
                              text="User : " + username, fg="steel blue", bd=10, anchor='w')
            userLabel.pack(side="right")

            handleDeconnect = self.deconnect
            deconnectBtn = Button(self, text='Log Out', bg='#31468F',
                                  fg='white', activebackground='#052B71',  font=('Inter', 40), command=handleDeconnect)
            deconnectBtn.pack(side="right")
            if store.isAdmin():
                handleCreationQuizz = self.createQuizzLink
                createQuizzBtn = Button(self, text='Create Quizz', font=('aria', 30, 'bold'), fg='steel blue', bd=0, anchor='w', command=handleCreationQuizz)
                createQuizzBtn.pack(side='right', padx=40, pady=40)
        else:
            buttonContainer = Frame(
                self, bg="#7FB8ED", borderwidth=0, height=450, width=855)
            buttonContainer.pack(side='right')

            signUpLink = self.getSignUpLink
            signUpBtn = Button(buttonContainer, text='Sign Up', bg='#31468F',
                               fg='black', activebackground='#052B71',  font=('Inter', 40), command=signUpLink)
            signUpBtn.pack(side="left", padx=20, pady=20)

            signInLink = self.getSignInLink
            signInBtn = Button(buttonContainer, text='Sign In', bg='#31468F',
                               fg='black', activebackground='#052B71',  font=('Inter', 40), command=signInLink)
            signInBtn.pack(side='right', padx=20, pady=20)
