from tkinter import *

class Template:

    def __init__(self):
        window = Tk()

        window.title("Quizz")
        window.geometry('1080x720')
        window.minsize(600,400)
        # window.iconbitmap('logo.png')

        document = Frame(window, bg="white",width = 1600,height=50,relief=SUNKEN)
        document.pack(expand=YES)

        self.window = window
        self.document = document

    def __createTopBar(self):
        Tops = Frame(self.document, bg="white",width = 1600,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

    def getWindow(self) -> Tk:
        return self.window

    def getDocument(self) -> Frame:
        return self.document

    def display(self) -> None:
        self.window.mainloop()

        