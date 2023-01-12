from tkinter import *
from views.components.Topbar import Topbar
from views.components.LblEntry import LblEntry
from store import store


class SignIn:
    def __init__(self, document):
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        store.getApp().setCurrentFrame('game')

    def __render(self):

        topbar = Topbar(self.document)
        topbar.pack()

        back = Frame(self.document, bg="#7FB8ED",
                     borderwidth=0, height=450, width=855)
        back.pack(expand=YES)

        userLblEntry = LblEntry(
            back, 'Username', '#7FB8ED', '#31468F', 28, 40, 20).getFrame()
        userLblEntry.place(x=60, y=82)

        pwLblEntry = LblEntry(back, 'Password', '#7FB8ED',
                              '#31468F', 28, 40, 20, True).getFrame()
        pwLblEntry.place(x=60, y=182)

        # pwLbl = Label(back, text='Password', bg='#7FB8ED', fg='#31468F', borderwidth=0, font=('Inter', 28))
        # pwLbl.place(x=60, y=182)

        # pwEntry= Entry(back, width=40, font=('arial',20))
        # pwEntry.place(x=240, y=182)

        SignInButton = Button(back, text='Sign In', bg='#31468F', fg='white',
                              activebackground='#052B71',  font=('Inter', 20), command=self.handleClick)
        SignInButton.place(x=350, y=360)

        pass
