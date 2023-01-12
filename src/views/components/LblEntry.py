from tkinter import *
from views.theme import THEME


class LblEntry(Frame):
    def __init__(self, parent, lblText, lblBgColor, lblFgColor, policeSize, entWidth, sizeEnt, show=False) -> None:
        super().__init__(parent, bg=THEME['lightBlue'])
        # self.frameLE = Frame(
        #     parent, bg=THEME['lightBlue'], width=1050, height=50)

        self.lbl = Label(self, text=lblText, bg=lblBgColor,
                         fg=lblFgColor, borderwidth=0, font=('Inter', policeSize))

        if show:
            self.entry = Entry(self, width=entWidth,
                               font=('inter', sizeEnt), show='*')
        else:
            self.entry = Entry(self, width=entWidth, font=('inter', sizeEnt))
        self.lbl.pack(side="left")
        self.entry.pack(side="right")
    
    def getEntry(self) -> Entry:
        return self.entry
