from tkinter import Canvas 
from Raw import Point, Tiles
import time 
from enum import Enum

class LightT(Enum):
    red = 0
    yellow = 1
    green = 2
    none = 3

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
            self.light = LightT.none


    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        points = [[self.x * 30, self.y * 30 + 8], [self.x * 30 + 8, self.y * 30], [self.x * 30 + 16, self.y * 30],
                  [self.x * 30 + 24, self.y * 30 + 8], [self.x * 30 + 24, self.y * 30 + 16], 
                  [self.x * 30 + 16, self.y * 30 + 24], [self.x * 30 + 8, self.y * 30 + 24], [self.x * 30, self.y * 30 + 16]]
        self.master.city.create_polygon(points, fill="red")
        self.master.city.create_text((self.x * 30 + 12, self.y * 30 + 11), text="S", fill="white")

    def draw_traffic_lights(self):
        self.master.city.create_rectangle(self.x * 30 + 2, self.y * 30 - 3, self.x * 30 + 18, self.y * 30 + 27, fill="black")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="grey")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="grey")
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="grey")

    def blink(self):
        if self.light == LightT.red: 
            self.greenOn()
            self.redOff()
        elif self.light == LightT.yellow:
            self.redOn()
            self.yellowOff()
        elif self.light == LightT.green:
            self.yellowOn()
            self.greenOff()

    def redOn(self):
        self.light = LightT.red
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="red")

    def redOff(self):
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="grey")

    def yellowOn(self):
        self.light = LightT.yellow
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="yellow")

    def yellowOff(self):
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="grey")

    def greenOn(self):
        self.light = LightT.green
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="green")

    def greenOff(self):
        self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="grey")

    '''
    #Traffic light change functions
    def redOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="red")
            self.master.update()
            time.sleep(0.05)

    def redOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="grey")
            self.master.update()
            time.sleep(0.05)

    def yellowOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="yellow")
            self.master.update()
            time.sleep(0.05)

    def yellowOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="grey")
            self.master.update()
            time.sleep(0.05)

    def greenOn(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="green")
            self.master.update()
            time.sleep(0.05)

    def greenOff(self, sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="grey")
            self.master.update()
            time.sleep(0.05)
    '''