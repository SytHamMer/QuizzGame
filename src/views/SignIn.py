from tkinter import *
from components.Topbar import Topbar
class SignIn:
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('game')

    def __render(self):

        topbar = Topbar(self.document)
        topbar.pack()
        

        back = Frame(self.document,bg= "#7FB8ED", borderwidth=0,height=450,width=855)
        back.pack(expand=YES)

        userLbl = Label(back, text='Username', bg='#7FB8ED', fg='#31468F', borderwidth=0, font=('Inter', 28))
        userLbl.place(x=60, y=82)

        userEntry=Entry(back, width=40, font=('arial',20))
        userEntry.place(x=240, y=82)

        pwLbl = Label(back, text='Password', bg='#7FB8ED', fg='#31468F', borderwidth=0, font=('Inter', 28))
        pwLbl.place(x=60, y=182)
        
        pwEntry= Entry(back, width=40, font=('arial',20))
        pwEntry.place(x=240, y=182)

        

        SignInButton = Button(back, text='Sign In',bg='#31468F', fg='white', activebackground='#052B71',  font=('Inter', 40), command=self.handleClick)
        SignInButton.place(x=350, y=320)

        pass