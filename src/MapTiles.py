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
    	#not finished yet still have to organize in the simulation.
        canvas = Canvas(self)
        canvas.create_rectangle(25,25,100,75, fill = "red")
        canvas.create_text((60,50), text="STOP")
        canvas.create_rectangle(50,25,100,75, fill = "red")

    def draw_traffic_lights(self):
        pass