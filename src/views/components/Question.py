from tkinter import *

from views.theme import THEME

class Question(Frame) :
    def __init__(self, nb, parent=None):
        Frame.__init__(self, parent)
        self.master.configure(bg=THEME['primary'], bd=20)

        self.pack()
        self.configure(bg=THEME['lightBlue'], bd=5)

        self.number = nb
 
        self.createWidgets()

    def createWidgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        questionNb = Label(self,text='Question ' + str(self.number), bg=THEME['lightBlue'], fg='white', font=('Inter',15))
        questionNb.grid(row=0)

        entryQuestion = Entry(self)
        entryQuestion.grid(row=1)

        answerLbl = Label(self,text='Réponse correcte', bg=THEME['lightBlue'], fg='white', font=('Inter',15))
        answerLbl.grid(row=2)

        answerEntry = Entry(self)
        answerEntry.grid(row=3)

        otherAns = Label(self,text='Autres réponses', bg=THEME['lightBlue'], fg='white', font=('Inter',15))
        otherAns.grid(row=4)

        ans1 = Entry(self)
        ans1.grid(row=5, padx=5, pady=5)
        ans2 = Entry(self)
        ans2.grid(row=6, padx=5, pady=5)
        ans3 = Entry(self)
        ans3.grid(row=7, padx=5, pady=5)
