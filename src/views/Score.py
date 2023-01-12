from tkinter import *
from unittest import result 
from views.theme import THEME
from store import store
from dbHandler import queryScore


class ScoreView:
    def __init__(self, document) -> None:
        self.document = document
        self.lblScore : Label | None = None
        self.__render()
    
    def getScore(self):
       return store.getScore()
   
    def getBestScore(self):
        bestScore = 0
        currentUser = 'ugo'
        allScore = queryScore(currentUser)
        for elt in allScore:
            if elt[3] > bestScore:
                bestScore = elt[3]
        return bestScore
            
               
    def __render(self):
        back = Frame(self.document, bg=THEME["lightBlue"],
                        borderwidth=0, height=471, width=450)
        back.pack(expand=YES)
        
        lblTitle = Label(back, text='Score', bg=THEME["lightBlue"], fg='#FFFFFF', font=('Inter', 50))
        lblTitle.place(x=140, y=34)
        
        score = self.getScore()
        self.lblScore = Label(back, text=f"{score}", bg=THEME["lightBlue"], fg='#31468F', font=('Inter', 50))
        self.lblScore.place(x=180, y=124)
        
        lblPoints = Label(back, text="points", bg=THEME["lightBlue"], fg='#31468F', font=('Inter', 15))
        lblPoints.place(x=195, y=190)
        
        bestScore = self.getBestScore()
        bestScoreLbl = Label(back, text=f"Your best : {bestScore} points", bg=THEME["lightBlue"], fg='#31468F', font=('Inter', 15))
        bestScoreLbl.place(x=40, y=290)
        
        btnMenu = Button(back, text="Menu", bg=THEME['lightBlue'], fg='#FFFFFF', font=('Inter', 20), padx=30, pady=10, bd=4)
        btnMenu.place(x=40, y=390)
        
        btnReplay = Button(back, text="Replay", bg='#31468F', fg='#FFFFFF', font=('Inter', 20), padx=30, pady=10, bd=4)
        btnReplay.place(x=250, y=390)