from tkinter import Canvas 
from Raw import Point, Tiles

class MapTiles(Canvas):
    def __init__(self, state, master=None):
        super().__init__(master=master)
        self.master = master
        self.state = state 
        if state == Tiles.stop_sign:
            self.draw_stop_sign()

    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        pass 

    def draw_traffic_lights(self):
        pass