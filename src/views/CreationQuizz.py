from tkinter import *

from views.components.Topbar import Topbar
from views.components.LblEntry import LblEntry
from views.components.QuestionFrame import QuestionFrame
from views.theme import THEME

class CreationQuizz :
    def __init__(self, document):
        self.document = document
        self.canvas= None
        self.mainFrame=None
        self.questionFrameContainer = None
        self.length = 2
        self.__render()

    def addQuestionFrame(self):
        container = self.questionFrameContainer
        if(container == None):
            raise Exception('questionFrameContainer is not defined.')
        newQuestion = QuestionFrame(self.length+1,parent=container)
        newQuestion.grid(column=self.length%2, row=self.length//2, padx = 50, pady = 10)
        self.length +=1
        self.mainFrame.update_idletasks()
        bbox = self.canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        self.canvas.configure(scrollregion=bbox, width=2060, height=1080)
        print(container.winfo_width())
    

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
        self.canvas = canvas

        #creation scrollbar
        scrollbar = Scrollbar(back, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=NS)
        canvas.configure(yscrollcommand=scrollbar.set)

        #
        mainFrame = Frame(canvas)
        self.mainFrame = mainFrame
        mainFrame.grid(row=0, column=0, sticky = N+S+E+W)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        #frame de label
        f1 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0,height=50,width=1080)
        f1.grid(row=0, sticky=N+E+W+S)

        homeLbl = Label(f1, text='Nouveau Quizz', bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 40, 'bold'), pady = 20)
        homeLbl.pack(anchor=CENTER)

        f2 = Frame(mainFrame,bg= THEME['primary'], borderwidth=20, height=200, width=1080)
        f2.grid(row=1, sticky=N+E+W+S)

        nom = LblEntry(f2, lblText='Nom', lblBgColor= THEME['primary'], lblFgColor=THEME['blueTopbar'], policeSize=20, entWidth= 20, sizeEnt=20)
        nom.grid(column=0, row=1, padx= 70)

        image = LblEntry(f2, lblText='Image', lblBgColor= THEME['primary'], lblFgColor=THEME['blueTopbar'], policeSize=20, entWidth= 20, sizeEnt=20)
        image.grid(column=1, row=1, padx=70)

        f3 = Frame(mainFrame,bg= THEME['primary'], borderwidth=0, width=1080)
        f3.grid(row=2, sticky=N+E+W+S)

        questionLbl = Label(f3, text='Questions :', bg=THEME['primary'], fg=THEME['blueTopbar'], borderwidth=0, font=('Inter', 28, 'bold'))
        questionLbl.grid(row=0, sticky=NW)

        questionFrameContainer = Frame(f3, bg='red')
        self.questionFrameContainer = questionFrameContainer
        questionFrameContainer.grid(columnspan=2, row=1, sticky=N+S+E+W)

        q1 = QuestionFrame(1,parent=questionFrameContainer)
        q1.grid(column=0, row=0, padx = 50, pady = 10)

        q2 = QuestionFrame(2,parent=questionFrameContainer)
        q2.grid(column=1, row=0, padx = 50, pady = 10)

        handleAddQuestion = self.addQuestionFrame
        addBtn = Button(f3, text='New Question', bg=THEME['lightBlue'], fg =THEME['blueTopbar'], font=("Inter", 50, 'bold'), command=handleAddQuestion)
        addBtn.grid(column=0, row=2)

        submitBtn = Button(f3, text='Submit', bg=THEME['blueTopbar'], fg = 'white', font=("Inter", 50, 'bold'))
        submitBtn.grid(column=1, row=2)

        canvas.create_window((0,0), window=mainFrame, anchor=NW)
        mainFrame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        canvas.configure(scrollregion=bbox, width=2060, height=1080)
