from Raw import Point, Turn

class Car:
    def __init__(self, coordinate : Point, dx, dy):
        self.x = coordinate.x
        self.y = coordinate.y
        self.dx = dx
        self.dy = dy 
        if dy == 1:
            self.state = Turn.down
        elif dx == 1:
            self.state = Turn.right
        elif dx == -1:
            self.state = Turn.left
        elif dy == -1:
            self.state = Turn.up
    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)
