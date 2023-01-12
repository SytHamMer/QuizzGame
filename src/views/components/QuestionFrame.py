from tkinter import *

from views.theme import THEME

class QuestionFrame(Frame) :
    def __init__(self, nb, parent=None):
        Frame.__init__(self, parent)
        self.master.configure(bg=THEME['primary'], bd=20)

        self.grid()
        self.configure(bg=THEME['lightBlue'], bd=15)

        self.number = nb
 
        self.createWidgets()

    def createWidgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        questionNb = Label(self,text='Question ' + str(self.number), bg=THEME['lightBlue'], fg='white', font=('Inter',20, 'bold'), bd=10)
        questionNb.grid(row=0)

        entryQuestion = Entry(self, width=40, font=('arial', 12))
        entryQuestion.grid(row=1)

        answerLbl = Label(self,text='Réponse correcte', bg=THEME['lightBlue'], fg='white', font=('Inter',15), bd=10)
        answerLbl.grid(row=2)

        answerEntry = Entry(self, width=40, font=('arial', 12))
        answerEntry.grid(row=3)

        otherAns = Label(self,text='Autres réponses', bg=THEME['lightBlue'], fg='white', font=('Inter',15), bd=10)
        otherAns.grid(row=4)

        ans1 = Entry(self, width=40, font=('arial', 12))
        ans1.grid(row=5, padx=10, pady=10)
        ans2 = Entry(self, width=40, font=('arial', 12))
        ans2.grid(row=6, padx=10, pady=10)
        ans3 = Entry(self, width=40, font=('arial', 12))
        ans3.grid(row=7, padx=10, pady=10)