from tkinter import Canvas 
from Raw import Point

class Tiles(Canvas):
    def __init__(self, master=None):
        super().__init__(master=master)

    def __repr__(self):
        return 'Tiles'