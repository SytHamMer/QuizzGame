from tkinter import *
from dbHandler import createAccount
from store import store
from views.components.Topbar import Topbar
from views.theme import THEME
from views.components.LblEntry import LblEntry


class SignUp:
    def __init__(self, document):
        self.document = document
        self.userEntry: Entry | None = None
        self.pwEntry: Entry | None = None
        self.cpwEntry: Entry | None = None
        self.checkboxVar: IntVar | None = None
        self.__render()

    def signUp(self) -> None:
        pseudoEntry = self.userEntry
        pwEntry = self.pwEntry
        cpwEntry = self.cpwEntry
        checkboxVar = self.checkboxVar

        if (pseudoEntry == None or pwEntry == None or cpwEntry == None or checkboxVar == None):
            raise Exception('One sign up is not defined')

        pseudo = pseudoEntry.get()
        pwd = pwEntry.get()
        isAdmin = checkboxVar.get()

        if (pwEntry.get() != cpwEntry.get()):
            print('password are different')
            return

        res = createAccount(pseudo, pwd, isAdmin)

        if (res != False):
            store.setUser(pseudo)
            store.getApp().setCurrentFrame('home')
        else:
            print('Failed to create a new account.')

    def __render(self):

        topbar = Topbar(self.document)
        topbar.pack()

        back = Frame(self.document, bg="#7FB8ED",
                     borderwidth=0, height=450, width=855)
        back.pack(expand=YES)

        userLblEntry = LblEntry(
            back, 'Username', THEME['lightBlue'], '#31468F', 28, 40, 20)
        self.userEntry = userLblEntry.getEntry()
        userLblEntry.place(x=10, y=10)

        pwLblEntry = LblEntry(
            back, 'Password', THEME['lightBlue'], '#31468F', 28, 40, 20, True)
        self.pwEntry = pwLblEntry.getEntry()
        pwLblEntry.place(x=10, y=110)

        cpwLblEntry = LblEntry(
            back, 'Confirm\nPassword', THEME['lightBlue'], '#31468F', 28, 40, 20, True)
        self.cpwEntry = cpwLblEntry.getEntry()
        cpwLblEntry.place(x=10, y=210)

        checkboxVar = IntVar()
        checkAdmin = Checkbutton(
            back, text='Administrateur', bg=THEME['lightBlue'], fg=THEME['blueTopbar'], font=('inter', 20), variable=checkboxVar)
        self.checkboxVar = checkboxVar
        checkAdmin.place(x=10, y=300)

        handleSignUp = self.signUp
        SignUpButton = Button(back, text='Sign Up', bg='#31468F', fg='white',
                              activebackground='#052B71',  font=('Inter', 20), command=handleSignUp)
        SignUpButton.place(x=350, y=360)

        self.userEntry.focus_force()
