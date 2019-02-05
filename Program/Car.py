from Raw import Point

class Car:
    def __init__(self, coordinate : Point, dx, dy, state):
        self.x = coordinate.x
        self.y = coordinate.y
        self.dx = dx
        self.dy = dy 
        self.state = state
    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)
