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
		points = [[0,50],[50,0],[100,0],[150,50],[150,100], [100,150],[50,150], [0,100]]
        canvas.create_polygon(points, fill = "red")
 	

    def draw_traffic_lights(self):
        pass