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
        self.master = master
        self.state = state
        if self.state == Tiles.car_left :
            self.draw_car_horizontal()
        elif self.state == Tiles.car_right : 
            self.draw_car_horizontal()
        self.update_speed()

    def __repr__(self):
        return 'Car : (x : {}, y : {}, dx : {}, dy : {}'.format(self.x, self.y, self.dx, self.dy)

    def update_speed(self):
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

    def update_state(self):
        if self.dx == 0 and self.dy == 1:
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_vertical()
        elif self.dx == 0 and self.dy == -1:
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_vertical()
        elif self.dx == 1 and self.dy == 0:
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_horizontal()
        else:
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_horizontal()

    def get_component(self):
        return self.__component

    def draw_car_horizontal(self):
        self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 30 + self.x * 30, 15 + self.y * 30, fill="yellow"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 15, self.y * 30 + 5, 23 + self.x * 30, 10 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 4 + self.x * 30, 7 + self.y * 30, fill="red"))
        self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30 + 8, 4 + self.x * 30, 15 + self.y * 30, fill="red"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 - 2, 12 + self.x * 30, 1 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 - 2, 27 + self.x * 30, 1 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 + 14, 12 + self.x * 30, 17 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 + 14, 27 + self.x * 30, 17 + self.y * 30, fill="black"))

    def draw_car_vertical(self):
        self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 15 + self.x * 30, 30 + self.y * 30, fill="yellow"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 5, self.y * 30 + 15, 10 + self.x * 30, 23 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 7 + self.x * 30, 4 + self.y * 30, fill="red"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 8, self.y * 30 , 15 + self.x * 30, 4 + self.y * 30, fill="red"))
        self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 7, 1 + self.x * 30, 12 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 22, 1 + self.x * 30, 27 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 7, 17 + self.x * 30, 12 + self.y * 30, fill="black"))
        self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 22, 17 + self.x * 30, 27 + self.y * 30, fill="black"))

    def turn_left(self):
        self.dx, self.dy = -self.dy, self.dx
        self.update_state()
        

    def turn_right(self):
        self.dx, self.dy = self.dy, -self.dx
        self.update_state()

    