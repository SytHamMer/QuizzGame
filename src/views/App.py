from tkinter import *
from views.theme import THEME


class App:

    def __init__(self, pages, defaultPage):
        window = Tk()

        window.title("Quizz")
        window.geometry('1080x720')
        window.minsize(600, 400)
        window.iconbitmap('src/views/logo.ico')
        window.config(background=THEME['primary'])

        documents = {}

        for slug in pages.keys():
            doc = Frame(window, bg=THEME['primary'])
            documents[slug] = doc
            pageDefiner = pages[slug]
            pageDefiner(self, doc)
            doc.pack(expand=YES)
            doc.place(in_=window, x=0, y=0,
                      relwidth=1, relheight=1)

        """ 
        Enable to know which frame is associatied to a page slug.
        """
        self.documents = documents

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

    def getDocument(self, slug) -> Frame:
        doc = self.documents[slug]
        if (doc == None):
            raise Exception("No document is linked to the slug " + slug)
        return doc

    def setCurrentFrame(self, slug) -> None:
        """Update the render of the App

        Args:
            slug (string): Slug of the new page.
        """
        for currentSlug in self.pages.keys():
            currentDoc = self.getDocument(currentSlug)
            if (currentSlug == slug):
                currentDoc.lift()

        self.currentFrame = slug

    def getCurrentFrame(self) -> str:
        return self.currentFrame

    def start(self) -> None:
        self.window.mainloop()
