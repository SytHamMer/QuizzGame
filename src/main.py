from dbHandler import createTables
from views.App import App
from views.Home import Home
from views.Game import Game
from views.SignIn import SignIn
from views.SignUp import SignUp

createTables()


app = App({
    'home': Home,
    'game': Game,
    'signin': SignIn,
    'signup': SignUp

}, 'signin')
app.start()
