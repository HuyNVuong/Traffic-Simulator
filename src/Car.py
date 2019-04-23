from tkinter import Canvas
from Raw import Point, Tiles

class Car(Canvas):
    
    def __init__(self, coordinate : Point, state : Tiles, master=None, dest=None, body='yellow'):
        super().__init__(master)
        self.x = coordinate.x
        self.y = coordinate.y
        self.pos = coordinate
        self.master = master
        self.state = state
        self.dest = dest
        self.color = body
        self.count = 0
        self.__component = []
        if self.state == Tiles.car_left :
            self.draw_car_horizontal_left()
        elif self.state == Tiles.car_right : 
            self.draw_car_horizontal_right()
        elif self.state == Tiles.car_up:
            self.draw_car_vertical_up()
        else: 
            self.draw_car_vertical_down()
        self.update_speed()

    def __repr__(self):
        return f'Car(x:{self.x}, y:{self.y}, state:{self.state}, master:{self.master}, dest:{self.dest}, color:{self.color})'

    def neighbors(self):
        raw_map = self.master.data
        
        return {raw_map[pos.y][pos.x] for pos in self.pos.neighbors()}

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
            self.state = Tiles.car_down
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_vertical_down()
        elif self.dx == 0 and self.dy == -1:
            self.state = Tiles.car_up
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_vertical_up()
        elif self.dx == 1 and self.dy == 0:
            self.state = Tiles.car_right
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_horizontal_right()
        else:
            self.state = Tiles.car_left
            for comp in self.__component:
                self.master.delete(comp)
            self.__component.clear() 
            self.draw_car_horizontal_left()

    def get_component(self):
        return self.__component

    def move(self):
        for comp in self.__component:
            self.master.city.move(comp, self.dx, self.dy)
        self.x += self.dx / 30
        self.y += self.dy / 30

    '''
    Drawing a component of car, with each component returns an integer value 
    as an index of that cars component
    >>> from Car import Car
    >>> from Map import Map
    >>> m = Map()
    >>> c = Car(Car(Point(5,8), Tiles.car_left)
    >>> c.get_components()
    [1,2,3,4,5,6,7,8]
    ''' 


    def draw_car_horizontal_right(self):
        if self.master:
           self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 30 + self.x * 30, 15 + self.y * 30, fill=self.color))
           self.__component.append(self.master.create_rectangle(self.x * 30 + 15, self.y * 30 + 5, 23 + self.x * 30, 10 + self.y * 30, fill="black"))
           self.__component.append(self.master.create_arc(self.x * 30 + 20, self.y * 30 + 15, 40 + self.x * 30, self.y * 30, start = 270, extent = 180, outline=self.color, fill=self.color))
           self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30 - 7, 6 + self.x * 30, 23 + self.y * 30, fill="red"))
           self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 - 2, 12 + self.x * 30, 1 + self.y * 30, fill="black"))
           self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 - 2, 27 + self.x * 30, 1 + self.y * 30, fill="black"))
           self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 + 14, 12 + self.x * 30, 17 + self.y * 30, fill="black"))
           self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 + 14, 27 + self.x * 30, 17 + self.y * 30, fill="black"))


    def draw_car_horizontal_left(self):
        if self.master:
            self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 30 + self.x * 30, 15 + self.y * 30, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 15, self.y * 30 + 5, 23 + self.x * 30, 10 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 28, self.y * 30 - 8, 35 + self.x * 30, 25 + self.y * 30, fill="red"))
            self.__component.append(self.master.create_arc(self.x * 30 + 22, self.y * 30 + 15.5,self.x * 30 -7, self.y * 30-1, start = 90, extent = 180, outline=self.color, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 - 2, 12 + self.x * 30, 1 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 - 2, 27 + self.x * 30, 1 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 7, self.y * 30 + 14, 12 + self.x * 30, 17 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 22, self.y * 30 + 14, 27 + self.x * 30, 17 + self.y * 30, fill="black"))

    def draw_car_vertical_up(self):
        if self.master:
            self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 15 + self.x * 30, 30 + self.y * 30, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 5, self.y * 30 + 15, 10 + self.x * 30, 23 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 - 8, self.y * 30 + 37, 23 + self.x * 30, 30 + self.y * 30, fill="red"))
            self.__component.append(self.master.create_arc(self.x * 30 -1, self.y * 30 - 6, 16 + self.x * 30, 17 +self.y * 30, start = 0, extent = 180, outline=self.color, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 7, 1 + self.x * 30, 12 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 22, 1 + self.x * 30, 27 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 7, 17 + self.x * 30, 12 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 22, 17 + self.x * 30, 27 + self.y * 30, fill="black"))

    def draw_car_vertical_down(self):
        if self.master:
            self.__component.append(self.master.create_rectangle(self.x * 30, self.y * 30, 15 + self.x * 30, 30 + self.y * 30, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 5, self.y * 30 + 15, 10 + self.x * 30, 23 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 25, self.y * 30 - 3,self.x * 30 - 8, 4 + self.y * 30, fill="red"))
            self.__component.append(self.master.create_arc(self.x * 30 + 16.5, self.y * 30 + 37,self.x * 30 -2, self.y * 30 + 6, start = 180, extent = 180, outline=self.color, fill=self.color))
            self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 7, 1 + self.x * 30, 12 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 - 2, self.y * 30 + 22, 1 + self.x * 30, 27 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 7, 17 + self.x * 30, 12 + self.y * 30, fill="black"))
            self.__component.append(self.master.create_rectangle(self.x * 30 + 14, self.y * 30 + 22, 17 + self.x * 30, 27 + self.y * 30, fill="black"))
            

    def turn_left(self):
        self.dx, self.dy = self.dy, -self.dx
        self.update_state()
        
    def turn_right(self):
        self.dx, self.dy = -self.dy, self.dx
        self.update_state()

    def stop(self):
        self.dx, self.dy = 0, 0

    def stop_for_three_step(self) -> bool:
        if self.count == 2:
            self.count = 0
            return False
        else:
            self.count += 1 
            self.dx, self.dy = 0, 0
            return True

if __name__ == "__main__":
    from tkinter import Tk
    root = Tk() 
    c = Canvas(master=root) 
    c.pack()
    sl = Car(Point(1,1), Tiles.car_right, master=c)
    root.mainloop()
    
