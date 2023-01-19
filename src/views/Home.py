from tkinter import *
from store import store

from dbHandler import *
from views.components.Topbar import Topbar
from views.theme import THEME

def adaptText(string, nbChar, nbLignes):
    res = ""
    l=1
    while len(string)>nbChar and l<nbLignes: 
        res += string[0:nbChar] + "\n"
        string = string[nbChar:len(string)]
        l+=1
    if len(string)>nbChar :
        string = string[0:nbChar]
    print(res+string)
    return res + string

class Home:
    def __init__(self, document):
        self.nbQuizz= len(queryQuizzs())
        self.document = document
        self.mainFrame = None
        self.__render()


    def initializeQuizzFrame(self) -> None:
        """method to initialize the frame containing every buttons that links to the quizz"""
        nbQuizz = self.nbQuizz
        #Frame creation
        f2 = Frame(self.mainFrame, bg=THEME['primary'], borderwidth=0, width=1080)
        f2.grid(row=1, sticky=N+S+E+W)

        for i in range(0, nbQuizz):
            quizzName = queryQuizzs()[i][0]
            def handleClick(name=quizzName):
                if not store.userIsLogged():
                    return
                store.targetQuizz(name)
                store.getApp().setCurrentFrame('game')
            text=adaptText(quizzName, 12, 3)
            btn = Button(f2, text=text, bg=THEME['lightBlue'], fg=THEME['blueTopbar'], padx=50, pady=50, font=(
                'Inter', 20, 'bold'), activebackground=THEME['blueTopbar'], activeforeground='white', width= 10, height=3, command=handleClick)
            btn.grid(row=i//3, column=i % 3, padx=20, pady=20)

    def __render(self) -> None:

        # ajout de la topbar
        topbar = Topbar(self.document)
        topbar.pack()

        # creation de la frame en dessous de la topbar
        back = Frame(
            self.document, bg=THEME['blueTopbar'], borderwidth=0, height=450, width=1080)
        back.pack(fill=BOTH)

        back.grid_rowconfigure(0, weight=1)
        back.grid_columnconfigure(0, weight=1)

        # creation d'une canvas pour la scrollbar
        canvas = Canvas(back, bg=THEME['primary'])
        canvas.grid(row=0, column=0)

        # creation scrollbar
        scrollbar = Scrollbar(back, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=NS)
        canvas.configure(yscrollcommand=scrollbar.set)

        #
        mainFrame = Frame(canvas)
        self.mainFrame = mainFrame
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)

        f1 = Frame(mainFrame, bg=THEME['primary'],
                   borderwidth=0, height=100, width=1080)
        f1.grid(row=0)

        homeLbl = Label(f1, text='Tous les quizz :',
                        bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 28, 'bold'))
        homeLbl.place(x=20, y=20)

        self.initializeQuizzFrame()



       

        canvas.create_window((0, 0), window=mainFrame, anchor=NW)
        mainFrame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        canvas.configure(scrollregion=bbox, width=2060, height=720)

