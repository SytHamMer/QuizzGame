# put here global data we need at anytime
from views.App import App


class Store:
    def __init__(self):
        self.selectedQuizz = None
        self.user: str | None = None
        self.app: App | None = None

    def setApp(self, app):
        self.app = app

    def setUser(self, user: str | None):
        self.user = user

    def getUser(self) -> str | None:
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
