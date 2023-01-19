from getpass import getuser
import threading
import time
from tkinter import *
from dbHandler import *
from store import store
from views.TabSystem import TabSystem
from views.theme import THEME
from views.components.Question import Question


class Game:
    def __init__(self, document):
        self.quizzName = store.getTargetedQuizz()
        self.document = document
        self.score = 0
        self.index = 0
        self.tabs: TabSystem | None = None
        self.scoreLabel: Label | None = None
        self.quizz = None

        # quizzName = 'foot'
        # questions = queryQuestionFromDB(quizzName)

        self.__render()

    def onChange(self, value, correctValue):
        if (value == correctValue):
            self.score += 1

            scoreLabel = self.scoreLabel
            if scoreLabel == None:
                raise Exception('scoreLabel is not defined.')
            scoreLabel.config(text=f"     Score : {self.score} points")

        tabs = self.tabs
        if (tabs == None):
            raise Exception('tabs is not defined')

        self.index += 1

        quizz = self.quizz
        if (quizz == None):
            raise Exception('quizz is not defined')

        print(quizz)

        if (len(quizz.keys()) <= self.index):
            self.exit()
        else:
            tabs.setTab(str(self.index))

    def exit(self):
        """Leave the Quizz at the end of it
        """
        store.setScore(self.score)
        majScore(store.getTargetedQuizz(),store.getUser(),self.score)
        store.getApp().setCurrentFrame("score")

    def __displayBottom(self):
        self.timer = 10  # take value of time in the creation of quizz
        self.finish = False

        def update_label(remaining):
            """Countdown        

            Args:
                remaining (int): timeleft
            """
            self.timer = remaining
            if remaining != 0:
                self.timer = remaining
                time.sleep(1)
                res = str(remaining)
                clock['text'] = f"Time left : {res} "
                t = threading.Thread(target=update_label, args=[remaining-1])
                t.start()
            else:
                self.timer = 1
                clock['text'] = "Time left : 1 "
                time.sleep(1)
                clock['text'] = "Time left : 0 "
                self.timer = 0
                self.exit()
                # self.finish = True
                # print(self.finish)
        # Il manque gestion des questions et points

        points = 0
        bottomframe = Frame(self.document, bg=THEME["primary"])
        timeleft = self.timer
        clock = Label(bottomframe, text=f"Time left :{timeleft}     ", bg=THEME["primary"], font=('Inter', 40),
                      fg=THEME["blueTopbar"], borderwidth=1)
        self.scoreLabel = Label(bottomframe, text=f"     Score : {points} points", bg=THEME["primary"], font=('Inter', 40),
                                fg=THEME["blueTopbar"])
        clock.grid(row=1, column=1)
        self.scoreLabel.grid(row=1, column=5)
        bottomframe.grid(row=2, pady=230)
        update_label(self.timer)

    def __render(self):

        topFrame = Frame(self.document, bg=THEME["primary"])
        
        # for quizz in self.quizz
        # question1 = {"question": "Qui est jaune ?", "reponses": [
        #     "poussin", "camion", "elephant", "poisson"], "bonneReponse": "poussin"}
        # question2 = {"question": "Qui est un urluberlu ? ", "reponses": [
        #     "Lila", "Mathys", "Ugo", "Arnaud"], "bonneReponse": "Mathys"}
        questions = queryQuestions(self.quizzName)
        quizz = {}

        handleChange = self.onChange
        for i in range(0, len(questions)):
            def createQuestion(parent, c=i):
                q = Question(parent, c, questions[c], handleChange)
                q.pack()
            quizz[str(i)] = createQuestion

        self.quizz = quizz

        self.tabs = TabSystem(topFrame, quizz, '0')
        topFrame.grid(row=1)

        self.__displayBottom()
