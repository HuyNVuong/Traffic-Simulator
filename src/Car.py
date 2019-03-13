import importlib
from tkinter import Canvas
from Raw import Point, Tiles
# importlib.import_module(Raw)

class Car(Canvas):
    __component = []
    def __init__(self, coordinate : Point, state : Tiles, master=None):
        super().__init__(master)
        self.x = coordinate.x
        self.y = coordinate.y
        self.state = state
        if self.state == Tiles.car_left :
            self.draw_car_horizontal()
        elif self.state == Tiles.car_right : 
            self.draw_car_horizontal()
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

    def get_component(self):
        return self.__component
    # def move(self):
    #     self.x += self.dx 
    #     self.y += self.dy 

    def draw_car_horizontal(self):
        # Car body
        self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 30 + self.x * 28, 15 + self.y * 29, fill="yellow"))
        # Car features
        self.__component.append(self.create_rectangle(self.x * 28 + 15, self.y * 29 + 5, 23 + self.x * 28, 10 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 4 + self.x * 28, 7 + self.y * 29, fill="red"))
        self.__component.append(self.create_rectangle(self.x * 28, self.y * 29 + 8, 4 + self.x * 28, 15 + self.y * 29, fill="red"))
        # 4 wheels
        self.__component.append(self.create_rectangle(self.x * 28 + 7, self.y * 29 - 2, 12 + self.x * 28, 1 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 + 22, self.y * 29 - 2, 27 + self.x * 28, 1 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 + 7, self.y * 29 + 14, 12 + self.x * 28, 17 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 + 22, self.y * 29 + 14, 27 + self.x * 28, 17 + self.y * 29, fill="black"))

    def draw_car_vertical(self):
        # Car bodself.y
        self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 15 + self.x * 28, 30 + self.y * 29, fill="yellow"))
        # Car features
        self.__component.append(self.create_rectangle(self.x * 28 + 5, self.y * 29 + 15, 10 + self.x * 28, 23 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 7 + self.x * 28, 4 + self.y * 29, fill="red"))
        self.__component.append(self.create_rectangle(self.x * 28 + 8, self.y * 29 , 15 + self.x * 28, 4 + self.y * 29, fill="red"))
        # 4 wheels
        self.__component.append(self.create_rectangle(self.x * 28 - 2, self.y * 29 + 7, 1 + self.x * 28, 12 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 - 2, self.y * 29 + 22, 1 + self.x * 28, 27 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 + 14, self.y * 29 + 7, 17 + self.x * 28, 12 + self.y * 29, fill="black"))
        self.__component.append(self.create_rectangle(self.x * 28 + 14, self.y * 29 + 22, 17 + self.x * 28, 27 + self.y * 29, fill="black"))

    def turn_left(self):
        if self.dx !=  0:
            # Car bodself.y
            self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 15 + self.x * 28, 30 + self.y * 29, fill="yellow"))
            # Car features
            self.__component.append(self.create_rectangle(self.x * 28 + 5, self.y * 29 + 15, 10 + self.x * 28, 23 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 7 + self.x * 28, 4 + self.y * 29, fill="red"))
            self.__component.append(self.create_rectangle(self.x * 28 + 8, self.y * 29 , 15 + self.x * 28, 4 + self.y * 29, fill="red"))
            # 4 wheels
            self.__component.append(self.create_rectangle(self.x * 28 - 2, self.y * 29 + 7, 1 + self.x * 28, 12 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 - 2, self.y * 29 + 22, 1 + self.x * 28, 27 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 + 14, self.y * 29 + 7, 17 + self.x * 28, 12 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 + 14, self.y * 29 + 22, 17 + self.x * 28, 27 + self.y * 29, fill="black"))
        else:
            # Car body
            self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 30 + self.x * 28, 15 + self.y * 29, fill="yellow"))
            # Car features
            self.__component.append(self.create_rectangle(self.x * 28 + 15, self.y * 29 + 5, 23 + self.x * 28, 10 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28, self.y * 29, 4 + self.x * 28, 7 + self.y * 29, fill="red"))
            self.__component.append(self.create_rectangle(self.x * 28, self.y * 29 + 8, 4 + self.x * 28, 15 + self.y * 29, fill="red"))
            # 4 wheels
            self.__component.append(self.create_rectangle(self.x * 28 + 7, self.y * 29 - 2, 12 + self.x * 28, 1 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 + 22, self.y * 29 - 2, 27 + self.x * 28, 1 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 + 7, self.y * 29 + 14, 12 + self.x * 28, 17 + self.y * 29, fill="black"))
            self.__component.append(self.create_rectangle(self.x * 28 + 22, self.y * 29 + 14, 27 + self.x * 28, 17 + self.y * 29, fill="black"))
            self.dx, self.dy = -self.dy, self.dx

    def turn_right(self):
        self.dx, self.dy = self.dy, -self.dx

    