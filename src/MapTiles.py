from tkinter import Canvas 
from Raw import Point, Tiles

class MapTiles(Canvas):
    def __init__(self, coordinate : Point, state, master=None):
        super().__init__(master=master)
        self.master = master
        self.state = state 
        self.x = coordinate.x
        self.y = coordinate.y
        if state == Tiles.stop_sign:
            self.draw_stop_sign()

    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        points = [[self.x * 30, self.y * 30 + 8],[self.x * 30 + 8, self.y * 30],[self.x * 30 + 16, self.y * 30],
                  [self.x * 30 + 24, self.y * 30 + 8],[self.x * 30 + 24, self.y * 30 + 16], 
                  [self.x * 30 + 16, self.y * 30 + 24],[self.x * 30 + 8, self.y * 30 + 24], [self.x * 30, self.y * 30 + 16]]
        self.master.city.create_polygon(points, fill = "red")
        self.master.city.create_text((self.x * 30 + 10, self.y * 30 + 10), text="STOP")


    def draw_traffic_lights(self):
        pass