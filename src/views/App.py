from tkinter import *
from views.theme import THEME
from views.TabSystem import TabSystem


class App(TabSystem):

    def __init__(self, pages, defaultPage):
        window = Tk()
        super().__init__(window, pages, defaultPage)

        window.title("Quizz")
        window.geometry('1080x720')
        window.minsize(600, 400)
        window.config(background=THEME['primary'])

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

    def setCurrentFrame(self, slug) -> None:
        """Update the render of the App

        Args:
            slug (string): Slug of the new page.
        """
        self.setTab(slug)

    def start(self) -> None:
        self.window.mainloop()
