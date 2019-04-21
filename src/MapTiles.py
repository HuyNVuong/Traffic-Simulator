from tkinter import Canvas 
from Raw import Point, Tiles
import time
import random
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
        self.pos = coordinate
        self.sl_light = LightT.none
        if state == Tiles.stop_sign:
            self.draw_stop_sign()
        elif state == Tiles.traffic_lights:
            self.draw_traffic_lights()
            self.light = LightT.none
        elif state == Tiles.sensor_light:
            self.draw_sensor_light()

    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        points = [[self.x * 30, self.y * 30 + 8], [self.x * 30 + 8, self.y * 30], [self.x * 30 + 16, self.y * 30],
                  [self.x * 30 + 24, self.y * 30 + 8], [self.x * 30 + 24, self.y * 30 + 16], 
                  [self.x * 30 + 16, self.y * 30 + 24], [self.x * 30 + 8, self.y * 30 + 24], [self.x * 30, self.y * 30 + 16]]
        self.master.create_polygon(points, fill="red")
        self.master.create_text((self.x * 30 + 12, self.y * 30 + 11), text="S", fill="white")

    def draw_traffic_lights(self):
        self.master.create_rectangle(self.x * 30 + 2, self.y * 30 - 3, self.x * 30 + 18, self.y * 30 + 27, fill="black")
        self.master.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="grey")
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="grey")
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="grey")
    
    def draw_dest_point(self, color):
        self.master.create_arc(self.x * 30 + 1, self.y * 30 + 40, self.x * 30 + 20, self.y * 30, start=0, extent=180, fill=color)
        self.master.create_text((self.x * 30 + 12, self.y * 30 + 11), text="A", fill="white")
        
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

    def sl_blink(self):
        if self.sl_light == LightT.red:
            self.greenOn()
            self.redOff()
        else:
            self.greenOff()
            self.redOn()

    def redOn(self):
        self.light = LightT.red
        self.master.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="red")

    def redOff(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30 - 3, self.x * 30 + 15, self.y * 30 + 7, fill="grey")

    def yellowOn(self):
        self.light = LightT.yellow
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="yellow")

    def yellowOff(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 7, self.x * 30 + 15, self.y * 30 + 17, fill="grey")

    def greenOn(self):
        self.light = LightT.green
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="green")

    def greenOff(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 17, self.x * 30 + 15, self.y * 30 + 27, fill="grey")

    def draw_sensor_light(self):
        self.master.create_rectangle(self.x * 30, self.y * 30 - 2, self.x * 30 + 22, self.y * 30 + 27, fill="black")
        self.master.create_oval(self.x * 30 + 5, self.y * 30, self.x * 30 + 17, self.y * 30 + 12, fill="grey")
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 13, self.x * 30 + 17, self.y * 30 + 25, fill="grey")
 
    def sl_redOn(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30, self.x * 30 + 17, self.y * 30 + 12, fill="red")
        self.sl_light = LightT.red

    def sl_redOff(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30, self.x * 30 + 17, self.y * 30 + 12, fill="grey")
        
    def sl_greenOn(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 13, self.x * 30 + 17, self.y * 30 + 25, fill="green")
        self.sl_light = LightT.green
    
    def sl_greenOff(self):
        self.master.create_oval(self.x * 30 + 5, self.y * 30 + 13, self.x * 30 + 17, self.y * 30 + 25, fill="grey")
   

if __name__ == "__main__":
    from tkinter import Tk
    root = Tk() 
    c = Canvas(master=root) 
    c.pack()
    sl = MapTiles(Point(1,1), Tiles.sensor_light, master=c)
    # sl.draw_traffic_lights()
    counter = 0
    while True:
        
        if counter % 1000 == 0:
            sl.sl_greenOn()
            sl.sl_redOff() 
        else:
            sl.sl_greenOn()
            sl.sl_redOff() 
        counter += 1
        c.update()
        root.update()
    root.mainloop()
