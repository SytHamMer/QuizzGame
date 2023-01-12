from tkinter import *

from views.components.Topbar import Topbar
from views.components.LblEntry import LblEntry
from views.components.Question import Question
from views.theme import THEME

class CreationQuizz :
    def __init__(self, app, document):
        self.app = app
        self.document = document
        self.__render()

    def handleClick(self) -> None:
        self.app.setCurrentFrame('game')

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

        #frame de label
        f1 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0,height=50,width=1080)
        f1.grid(row=0)

        homeLbl = Label(f1, text='Nouveau Quizz', bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 28, 'bold'))
        homeLbl.pack(anchor = CENTER)

        f2 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0, height=200, width=1080)
        f2.grid(row=1)

        nom = LblEntry(f2, lblText='Nom', lblBgColor= THEME['primary'], lblFgColor=THEME['blueTopbar'], policeSize=20, entWidth= 50, sizeEnt=20)
        nom.grid(column=0)

        image = LblEntry(f2, lblText='Image', lblBgColor= THEME['primary'], lblFgColor=THEME['blueTopbar'], policeSize=20, entWidth= 50, sizeEnt=20)
        image.grid(column=1)

        f3 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0, width=1080)
        f3.grid(row=2)

        questionLbl = Label(f3, text='Questions :', bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 28, 'bold'))
        questionLbl.grid(row=0)
        
        test = Question(1,parent=f3)
        test.grid(row=1)

        # handler = self.handleClick

        # for i in range(0, nbQuizz):
        #     btn = Button(f2, text = "Quizz", bg=THEME['lightBlue'], fg=THEME['blueTopbar'], padx=100, pady=50, font=('Inter', 20, 'bold'), activebackground=THEME['blueTopbar'], activeforeground='white', command=handler)
        #     btn.grid(row=i//3, column = i%3, padx= 20, pady= 20)

        canvas.create_window((0,0), window=mainFrame, anchor=NW)
        mainFrame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        canvas.configure(scrollregion=bbox, width=2060, height=720)
