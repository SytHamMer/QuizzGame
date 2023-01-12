from tkinter import *
from store import store

from views.components.Topbar import Topbar
from views.theme import THEME

nbQuizz = 10
nbRows = nbQuizz//3


class Home:
    def __init__(self, document):
        print('HOMe is rendred')
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        store.getApp().setCurrentFrame('game')

    def __render(self) -> None:

        #ajout de la topbar
        topbar = Topbar(self.document)
        topbar.pack()

        #creation de la frame en dessous de la topbar
        back = Frame(self.document,bg= THEME['blueTopbar'], borderwidth=0,height=450,width=1080)
        back.pack(fill=BOTH)

        back.grid_rowconfigure(0, weight=1)
        back.grid_columnconfigure(0, weight=1)

        #creation d'une canvas pour la scrollbar
        canvas = Canvas(back, bg=THEME['primary'])
        canvas.grid(row=0, column=0)

        #creation scrollbar
        scrollbar = Scrollbar(back, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=NS)
        canvas.configure(yscrollcommand=scrollbar.set)

        #
        mainFrame = Frame(canvas)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)

        f1 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0,height=100,width=1080)
        f1.grid(row=0)

        homeLbl = Label(f1, text='Tous les quizz :',
                        bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 28, 'bold'))
        homeLbl.place(x=20, y=20)

        f2 = Frame(mainFrame, bg=THEME['primary'], borderwidth=0, width=1080)
        f2.grid(row=1, sticky=N+S+E+W)

        handler = self.handleClick

        for i in range(0, nbQuizz):
            btn = Button(f2, text="Quizz", bg=THEME['lightBlue'], fg=THEME['blueTopbar'], padx=100, pady=50, font=(
                'Inter', 20, 'bold'), activebackground=THEME['blueTopbar'], activeforeground='white', command=handler)
            btn.grid(row=i//3, column=i % 3, padx=20, pady=20)

        canvas.create_window((0, 0), window=mainFrame, anchor=NW)
        mainFrame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        canvas.configure(scrollregion=bbox, width=2060, height=720)
