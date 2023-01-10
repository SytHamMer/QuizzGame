from tkinter import *
from views.theme import THEME

class LblEntry(Frame):
    def __init__(self, parent,lblText, lblBgColor, lblFgColor, policeSize, entWidth, sizeEnt) -> None:
        super().__init__(parent, bg=THEME['lightBlue'])
        self.frameLE = Frame(parent, bg=THEME['lightBlue'], width=1050, height=50)
        
        
        
        self.lbl = Label(self.frameLE, text=lblText, bg=lblBgColor, fg=lblFgColor, borderwidth=0, font=('Inter', policeSize))
        
        self.entry = Entry(self.frameLE, width=entWidth, font=('arial',sizeEnt))
        self.lbl.pack(side="left")
        self.entry.pack(side="right")
        
    def getFrame(self):
        return self.frameLE
        
    

        
