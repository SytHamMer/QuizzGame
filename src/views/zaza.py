from tkinter import *

from views.components.Topbar import Topbar


class Home:
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('game')

    def __render(self) -> None:
        topbar = Topbar(self.document)
        topbar.pack()

        lblDrinks = Label(self.document, font=('aria', 16, 'bold'),
                          text="Home page", fg="steel blue", bd=10, anchor='w')
        lblDrinks.pack()

        handler = self.handleClick
        btn7 = Button(self.document, padx=16, pady=16, bd=4, fg="black", font=(
            'ariel', 20, 'bold'), command=handler)
        btn7.pack()
