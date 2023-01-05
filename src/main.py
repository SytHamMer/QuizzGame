from views.App import App
from views.Home import Home
from views.Game import Game

app = App({
    'home': Home,
    'game': Game
}, 'game')
app.start()
