from tkinter import *
from turtle import window_height, window_width

class SignIn:
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('signIn')

    def __render(self):
        back = Frame(self.document,bg= "#7FB8ED", borderwidth=0,height=200,width=200)
        back.pack(expand=YES)
