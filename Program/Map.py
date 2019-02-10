from appJar import gui
from typing import List
from Car import Car
from Raw import raw_map, Unit, Point, Turn
from ActionListener import actionListenter

# Map class to create a map simulation, map inherit method from GUI class from appJar
# Map __init__ got re-implement to generate a road map right when we initilize a new map
class Map(gui):
    
    def __init__(self):
        super().__init__("Traffic Simulator", "790x830")
        self.setBg("#ffe4b5")
        # self.setSticky("nw")
        commandCenter = self.addCanvas("commandCenter", 0, 0, 5, 1)
        # self.addLabel("CarNum", "Number of cars", 0, 0)
        # self.addLabel("TimeElapsed", "Time Elapsed: ", 0, 1)
        # self.addButton("Start", actionListenter(), 1, 0)
        # self.addButton("Stop", actionListenter(), 1, 1)
        # self.addButton("Reset", actionListenter(), 1, 2)
        self.map = self.addCanvas("map", 1, 0, 5, 5)
        
        # self.setSticky("both")
    def paint(self):
        for y in range(len(raw_map)):
            for x in range(len(raw_map[y])):
                if (raw_map[y][x] == Unit.wall):    
                    self.draw_block(x, y)
                elif(raw_map[y][x] == Turn.up):
                    self.draw_car_vertical(x, y)
                elif(raw_map[y][x] == Turn.left):
                    self.draw_car_horizontal(x, y)
                # else:
                #     self.draw_dot(canvas, x, y)

    def draw_block(self, x, y):
        self.map.create_rectangle(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="black", fill="#808080")
        # self.draw_dot(x, y)

    def draw_car_horizontal(self, x , y):
        # Car body
        self.map.create_rectangle(x * 28, y * 29, 30 + x * 28, 15 + y * 29, fill="yellow")
        # Car features
        self.map.create_rectangle(x * 28 + 15, y * 29 + 5, 23 + x * 28, 10 + y * 29, fill="black")
        self.map.create_rectangle(x * 28, y * 29, 4 + x * 28, 7 + y * 29, fill="red")
        self.map.create_rectangle(x * 28, y * 29 + 8, 4 + x * 28, 15 + y * 29, fill="red")
        # 4 wheels
        self.map.create_rectangle(x * 28 + 7, y * 29 - 2, 12 + x * 28, 1 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 + 22, y * 29 - 2, 27 + x * 28, 1 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 + 7, y * 29 + 14, 12 + x * 28, 17 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 + 22, y * 29 + 14, 27 + x * 28, 17 + y * 29, fill="black")

    def draw_car_vertical(self, x, y):
        # Car body
        self.map.create_rectangle(x * 28, y * 29, 15 + x * 28, 30 + y * 29, fill="yellow")
        # Car features
        self.map.create_rectangle(x * 28 + 5, y * 29 + 15, 10 + x * 28, 23 + y * 29, fill="black")
        self.map.create_rectangle(x * 28, y * 29, 7 + x * 28, 4 + y * 29, fill="red")
        self.map.create_rectangle(x * 28 + 8, y * 29 , 15 + x * 28, 4 + y * 29, fill="red")
        # 4 wheels
        self.map.create_rectangle(x * 28 - 2, y * 29 + 7, 1 + x * 28, 12 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 - 2, y * 29 + 22, 1 + x * 28, 27 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 + 14, y * 29 + 7, 17 + x * 28, 12 + y * 29, fill="black")
        self.map.create_rectangle(x * 28 + 14, y * 29 + 22, 17 + x * 28, 27 + y * 29, fill="black")

    def draw_dot(self, x, y):
        self.map.create_rectangle(x * 28 + 10, y * 29 + 10, x * 28 + 16, y * 29 + 16, fill="#fff")

    def add_car(self, car):
        y, x = car.y, car.x
        raw_map[y][x] = car.state

    def open_spot(self):
        open_spot : List[Point]
        for y, row in enumerate(raw_map):
            for x, spot in enumerate(row):
                if spot == 0:
                    open_spot.append(Point(x, y))
        return open_spot

# Testing purpose
if __name__ == "__main__":   
    map = Map()
    map.go()