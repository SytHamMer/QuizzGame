from dbHandler import createTables
from views.App import App
from views.Home import Home
from views.Game import Game
from views.SignIn import SignIn
from views.SignUp import SignUp
from store import store

createTables()

app = App({
    'home': Home,
    'game': Game,
    'signin': SignIn,
    'signup': SignUp
<<<<<<< HEAD

}, 'game')
=======
}, 'signin')

store.setApp(app)

>>>>>>> 95b84ba7119db293d42253148c7d0c4fed569e24
app.start()
