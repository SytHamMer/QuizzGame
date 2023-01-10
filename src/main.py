#from dbHandler import createTables
from views.App import App
from views.Home import Home
from views.Game import Game
from views.SignIn import SignIn
from views.SignUp import SignUp



app = App({
    'home': Home,
    'game': Game,
    'signin': SignIn,
    'signup': SignUp

}, 'game')
app.start()
