from views.App import App
from views.zaza import Home
from views.rrrr import Game
from views.SignIn import SignIn
from views.SignUp import SignUp

app = App({
    'home': Home,
    'game': Game,
    'signin' : SignIn,
    'signup' : SignUp

}, 'signin')
app.start()
