from tkinter import *
from views.components.Question import Question
from views.theme import THEME

class Questionnaire(Frame):
    def __init__(self,parent,name):
        self.name = name
        self.parent = parent
        question1 = {"question": "Qui est jaune ?","reponses":["poussin","camion","elephant","poisson"],"bonneReponse": "poussin"}
        question2 = {"question": "Qui est gentil ? ","reponses":["Lila","Mathys","Ugo","Arnaud"],"bonneReponse": "Mathys"}
        questions = [question1,question2]
        quizz = {}
        i=0
        for slug in quizz.keys():
            questionContainer = Frame(self, bg=THEME['primary'])
            Question(questionContainer,i,questions[i])
            
            quizz[slug] = questionContainer
            questionContainer.pack(expand=YES)
            questionContainer.place(in_=parent, x=0, y=0,
                      relwidth=1, relheight=1)
            i = i+1
            
            self.quizz = quizz
    def setCurrentFrame(self, slug):

        for currentSlug in self.quizz.keys():
            currentDoc = self.quizz[currentSlug]
            if (currentSlug == slug):
                currentDoc.lift()

        self.currentFrame = slug
                
    def getCurrentFrame(self):
        return self.currentFrame
    
    