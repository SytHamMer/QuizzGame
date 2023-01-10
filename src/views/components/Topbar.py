from tkinter import *
from views.theme import THEME


class Topbar(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent, bg=THEME['blueTopbar'], height=100)

    def pack(self) -> None:
        super().pack(side="top", fill="x")
