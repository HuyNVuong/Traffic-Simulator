from tkinter import Canvas 
from Raw import Point, Tiles
import time 

class MapTiles(Canvas):


    def __init__(self, coordinate : Point, state, master=None):
        super().__init__(master=master)
        self.master = master
        self.state = state 
        self.x = coordinate.x
        self.y = coordinate.y
        if state == Tiles.stop_sign:
            self.draw_stop_sign()
        elif state == Tiles.traffic_lights:
            self.draw_traffic_lights()

    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        points = [[self.x * 30, self.y * 30 + 8],[self.x * 30 + 8, self.y * 30],[self.x * 30 + 16, self.y * 30],
                  [self.x * 30 + 24, self.y * 30 + 8],[self.x * 30 + 24, self.y * 30 + 16], 
                  [self.x * 30 + 16, self.y * 30 + 24],[self.x * 30 + 8, self.y * 30 + 24], [self.x * 30, self.y * 30 + 16]]
        self.master.city.create_polygon(points, fill = "red")
        self.master.city.create_text((self.x * 30 + 10, self.y * 30 + 10), text="STOP")


    def draw_traffic_lights(self):
        self.master.city.create_rectangle(self.x * 30 , self.y * 30 - 5, self.x * 30 + 20, self.y * 30 + 35, fill="black")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30, self.x * 30 + 15, self.y * 30 + 10, fill="grey")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 11, self.x * 30 + 15, self.y * 30 + 21, fill="grey")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 22, self.x * 30 + 15, self.y * 30 + 32, fill="grey")

    

    #Traffic light change functions
    def redOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30 + 5, self.y * 30, self.x * 30 + 15, self.y * 30 + 10, fill="red")
            self.master.update()
            time.sleep(0.05)

    def redOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            self.master.update()
            time.sleep(0.05)

    def yellowOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 11, self.x * 30 + 15, self.y * 30 + 21, fill="yellow")
            self.master.update()
            time.sleep(0.05)

    def yellowOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            self.master.update()
            time.sleep(0.05)

    def greenOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 22, self.x * 30 + 15, self.y * 30 + 32, fill="green")
            self.master.update()
            time.sleep(0.05)

    def greenOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            self.master.update()
            time.sleep(0.05)
