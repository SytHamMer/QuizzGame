from Template import Template
from theme import THEME
from tkinter import *


class Sub_Template(Template):
    """
    The class which represent the top-bar template
    """    

    def __init__(self):
        super().__init__()
        TopBar = Frame(self.getDocument(), bg=THEME['blue_topbar'], width=self.getWindow().winfo_width(), height=100)
        TopBar.pack(side=TOP)
