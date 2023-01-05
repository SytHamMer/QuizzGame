from views.App import App
from views.Home import Home
from views.Game import Game
from views.SignIn import SignIn

app = App({
    'home': Home,
    'game': Game,
    'signin' : SignIn
}, 'signin')
app.start()
