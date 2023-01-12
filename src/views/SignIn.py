from tkinter import *
from dbHandler import connectUser
from views.components.Topbar import Topbar
from views.components.LblEntry import LblEntry
from store import store


class SignIn:
    def __init__(self, document):
        self.document = document
        self.userEntry: Entry | None = None
        self.pwEntry: Entry | None = None
        self.__render()

    def signIn(self) -> None:
        pseudoEntry = self.userEntry
        pwEntry = self.pwEntry

        if (pseudoEntry == None or pwEntry == None):
            raise Exception('One sign in is not defined')

        pseudo = pseudoEntry.get()
        pwd = pwEntry.get()

        res = connectUser(pseudo, pwd)

        if (res != False):
            store.setUser(pseudo)
            store.getApp().setCurrentFrame('home')

    def __render(self):

        topbar = Topbar(self.document)
        topbar.pack()

        back = Frame(self.document, bg="#7FB8ED",
                     borderwidth=0, height=450, width=855)
        back.pack(expand=YES)

        userLblEntry = LblEntry(
            back, 'Username', '#7FB8ED', '#31468F', 28, 40, 20)
        self.userEntry = userLblEntry.getEntry()
        userLblEntry.place(x=60, y=82)

        pwLblEntry = LblEntry(back, 'Password', '#7FB8ED',
                              '#31468F', 28, 40, 20, True)
        self.pwEntry = pwLblEntry.getEntry()
        pwLblEntry.place(x=60, y=182)

        handleSignIn = self.signIn
        SignInButton = Button(back, text='Sign In', bg='#31468F', fg='white',
                              activebackground='#052B71',  font=('Inter', 20), command=handleSignIn)
        SignInButton.place(x=350, y=360)

        self.userEntry.focus_force()
