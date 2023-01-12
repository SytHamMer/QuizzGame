from tkinter import *
from views.components.Questionnaire import Questionnaire
from views.theme import THEME
from views.components.Question import Question
from model.Timer import Timer



class Game:
    def __init__(self, app, document):

        self.app = app
        self.document = document
        self.timer = Timer(60) 

        
       # quizzName = 'foot'
       # questions = queryQuestionFromDB(quizzName)  
        
        self.__render()



    def __render(self):

        #Il manque gestion des questions et points
        
        questionnaire = Questionnaire(self.document,"test")
        questionnaire.pack()
        points = 0 
        bottomframe = Frame(self.document,bg = THEME["primary"])
        timeleft = self.timer.getTime()[0]
        clock  = Label(bottomframe,text = f"Time left :{timeleft}     ",bg =  THEME["primary"],font = ('Inter', 40),
                       fg = THEME["blueTopbar"],borderwidth=1)
        score = Label(bottomframe,text = f"     Score : {points} points",bg = THEME["primary"],font = ('Inter', 40),
                       fg = THEME["blueTopbar"])
        clock.grid(row=1,column=1)

        score.grid(row=1,column=5)
        bottomframe.grid(row=2,pady=230)






