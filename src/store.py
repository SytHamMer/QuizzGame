# put here global data we need at anytime
from views.App import App


class Store:
    def __init__(self):
        self.selectedQuizz = None
        self.user = None
        self.app: App | None = None

    def setApp(self, app):
        self.app = app

    def setUser(self, user):
        self.user = user

    def setSelectedQuizz(self, selectedQuizz):
        self.selectedQuizz = selectedQuizz

    def getApp(self) -> App:
        app = self.app
        if (app == None):
            raise Exception('App is not defined.')
        return app


store = Store()
