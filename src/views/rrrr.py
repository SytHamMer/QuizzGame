from tkinter import *


class Game:
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('home')

    def __render(self) -> None:

        lblDrinks = Label(self.document, font=('aria', 16, 'bold'),
                          text="Game page", fg="steel blue", bd=10, anchor='w')
        lblDrinks.pack()

        handler = self.handleClick
        btn7 = Button(self.document, padx=16, pady=16, bd=4, fg="orange", background="blue", font=(
            'ariel', 20, 'bold'), command=handler)
        btn7.pack()
