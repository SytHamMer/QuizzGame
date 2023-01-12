# put here global data we need at anytime
from logging import exception
from views.App import App


class Store:
    def __init__(self):
        self.selectedQuizz = None
        self.user: str | None = None
        self.app: App | None = None
        self.targetedQuizz: str | None = 'test'
        self.score : str | None= None


    def setApp(self, app):
        self.app = app

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def targetQuizz(self, targetedQuizz: str | None):
        self.targetedQuizz = targetedQuizz

    def getTargetedQuizz(self) -> str:
        quizzName = self.targetedQuizz
        if (quizzName == None):
            raise Exception('quizzName is not defined.')
        return quizzName

    def userIsLogged(self) -> bool:
        return self.user != None

    def setSelectedQuizz(self, selectedQuizz):
        self.selectedQuizz = selectedQuizz

    def getApp(self) -> App:
        app = self.app
        if (app == None):
            raise Exception('App is not defined.')
        return app

    def setScore(self, score):
        self.score = score

    def getScore(self) -> str:
        score = self.score
        if score == None:
            raise Exception("Score is not defined")
        return score
    


store = Store()
