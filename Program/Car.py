from Raw import Point, Turn

class Car:
    def __init__(self, coordinate : Point, state):
        self.x = coordinate.x
        self.y = coordinate.y
        self.state = state
        self.dx = 0
        self.dy = 0
    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)
