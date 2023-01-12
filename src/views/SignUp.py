from tkinter import *
from views.components.Topbar import Topbar
from views.theme import THEME
from views.components.LblEntry import LblEntry


class SignUp:
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('game')

    def __render(self):

        topbar = Topbar(self.document)
        topbar.pack()

        back = Frame(self.document, bg="#7FB8ED",
                     borderwidth=0, height=450, width=855)
        back.pack(expand=YES)

        UserLblEntry = LblEntry(
            back, 'Username', THEME['lightBlue'], '#31468F', 28, 40, 20).getFrame()
        UserLblEntry.place(x=10, y=10)

        pwLblEntry = LblEntry(
            back, 'Password', THEME['lightBlue'], '#31468F', 28, 40, 20, True).getFrame()
        pwLblEntry.place(x=10, y=110)

        cpwLblEntry = LblEntry(
            back, 'Confirm\nPassword', THEME['lightBlue'], '#31468F', 28, 40, 20, True).getFrame()
        cpwLblEntry.place(x=10, y=210)

        checkAdmin = Checkbutton(
            back, text='Administrateur', bg=THEME['lightBlue'], fg=THEME['blueTopbar'], font=('inter', 20))
        checkAdmin.place(x=10, y=300)

        SignUpButton = Button(back, text='Sign Up', bg='#31468F', fg='white',
                              activebackground='#052B71',  font=('Inter', 20), command=self.handleClick)
        SignUpButton.place(x=350, y=360)
