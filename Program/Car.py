import importlib
from Raw import *
# importlib.import_module(Raw)

class Car:
    def __init__(self, coordinate : Point, state : Tiles):
        self.x = coordinate.x
        self.y = coordinate.y
        self.state = state
        self.init_speed()

    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)

    def init_speed(self):
        if self.state == Tiles.car_down:
            self.dy, self.dx = 1, 0
        elif self.state == Tiles.car_up:
            self.dy, self.dx = -1, 0
        elif self.state == Tiles.car_left:
            self.dy, self.dx = 0, -1
        elif self.state == Tiles.car_right:
            self.dy, self.dx = 0, 1
        else:
            self.dy, self.dx = 0, 0

    def move(self):
        self.x += self.dx 
        self.y += self.dy 

