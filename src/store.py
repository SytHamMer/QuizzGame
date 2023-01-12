# put here global data we need at anytime
from views.App import App


class Store:
    def __init__(self):
        self.selectedQuizz = None
        self.user = None
        self.app = None

    def setApp(self, app):
        self.app = app

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def userIsLogged(self) -> bool:
        return self.user != None

    def setSelectedQuizz(self, selectedQuizz):
        self.selectedQuizz = selectedQuizz

    def getApp(self) -> App:
        app = self.app
        if (app == None):
            raise Exception('App is not defined.')
        return app


store = Store()
