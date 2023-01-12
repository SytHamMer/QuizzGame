from tkinter import *

from views.theme import THEME
import random
class QuestionFrame(Frame) :
    def __init__(self, nb, parent=None):
        Frame.__init__(self, parent)
        self.master.configure(bg=THEME['primary'], bd=20)
        self.questionEntry= None
        self.answerEntry = None
        self.ans1 = None
        self.ans2 = None
        self.ans3 = None

        self.grid()
        self.configure(bg=THEME['lightBlue'], bd=15)

        self.number = nb
 
        self.createWidgets()

    def createWidgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        questionNb = Label(self,text='Question ' + str(self.number), bg=THEME['lightBlue'], fg='white', font=('Inter',20, 'bold'), bd=10)
        questionNb.grid(row=0)

        self.entryQuestion = Entry(self, width=40, font=('arial', 12))
        self.entryQuestion.grid(row=1)

        answerLbl = Label(self,text='Réponse correcte', bg=THEME['lightBlue'], fg='white', font=('Inter',15), bd=10)
        answerLbl.grid(row=2)

        self.answerEntry = Entry(self, width=40, font=('arial', 12))
        self.answerEntry.grid(row=3)

        self.otherAns = Label(self,text='Autres réponses', bg=THEME['lightBlue'], fg='white', font=('Inter',15), bd=10)
        self.otherAns.grid(row=4)

        self.ans1 = Entry(self, width=40, font=('arial', 12))
        self.ans1.grid(row=5, padx=10, pady=10)
        self.ans2 = Entry(self, width=40, font=('arial', 12))
        self.ans2.grid(row=6, padx=10, pady=10)
        self.ans3 = Entry(self, width=40, font=('arial', 12))
        self.ans3.grid(row=7, padx=10, pady=10)
        
    def getData(self):
        listAnswer = [self.ans1.get(), self.ans2.get(), self.ans3.get(), self.answerEntry.get()]
        random.shuffle(listAnswer)
        dico = {'question' : self.entryQuestion.get(), 'reponses' : listAnswer, 'bonneReponse': self.answerEntry}
        return dico
        