from tkinter import *
from views.theme import THEME


class App:

    def __init__(self, pages, defaultPage):
        window = Tk()

        window.title("Quizz")
        window.geometry('1080x720')
        window.minsize(600, 400)
        window.config(background=THEME['primary'])

        """ 
        Enable to know which frame is associatied to a pageDefiner.
        """
        self.pages = pages
        """
        Slug of the current displayed frame.
        """
        self.currentFrame = defaultPage
        """ 
        Window of the App
        """
        self.window = window
        self.setCurrentFrame(self.currentFrame)

    def getWindow(self) -> Tk:
        return self.window

    def getCurrentDocument(self) -> Frame:
        return self.currentDocument

    def setCurrentFrame(self, slug) -> None:
        """Update the render of the App

        Args:
            slug (string): Slug of the new page.
        """

        for widget in self.window.winfo_children():
            widget.destroy()

        pageDefiner = self.pages[slug]
        self.currentDocument = pageDefiner(self.window)
        self.currentFrame = slug

    def getCurrentFrame(self) -> str:
        return self.currentFrame

    def start(self) -> None:
        self.window.mainloop()
