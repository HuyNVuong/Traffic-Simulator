
class Car:
    def __init__(self, x, y, dx, dy, state):
        self.x = x
        self.y = y 
        self.dx = dx
        self.dy = dy 
        self.state = state
    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)
