from appJar import gui
from Raw import raw_map, Unit

# Map class to create a map simulation, map inherit method from GUI class from appJar
# Map __init__ got re-implement to generate a road map right when we initilize a new map
class Map(gui):
    def __init__(self):
        super().__init__("Traffic Simulator", "790x830")
        self.setBg("#ffe4b5")
        canvas = self.addCanvas("canvas")
        for y in range(len(raw_map)):
            for x in range(len(raw_map[y])):
                if (raw_map[y][x] == Unit.wall):    
                    canvas.create_oval(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="black", fill="#808080")
                elif(raw_map[y][x] == Unit.vertical_car):
                    self.draw_car_vertical(canvas, x, y)
                elif(raw_map[y][x] == Unit.horizontal_car):
                    self.draw_car_horizontal(canvas, x, y)
                else:
                    self.draw_dot(canvas, x, y)
    
    def draw_car_horizontal(self, canvas, x , y):
        # Car body
        canvas.create_rectangle(x * 28, y * 29, 30 + x * 28, 15 + y * 29, fill="yellow")
        # Car features
        canvas.create_rectangle(x * 28 + 15, y * 29 + 5, 23 + x * 28, 10 + y * 29, fill="black")
        canvas.create_rectangle(x * 28, y * 29, 4 + x * 28, 7 + y * 29, fill="red")
        canvas.create_rectangle(x * 28, y * 29 + 8, 4 + x * 28, 15 + y * 29, fill="red")
        # 4 wheels
        canvas.create_rectangle(x * 28 + 7, y * 29 - 2, 12 + x * 28, 1 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 + 22, y * 29 - 2, 27 + x * 28, 1 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 + 7, y * 29 + 14, 12 + x * 28, 17 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 + 22, y * 29 + 14, 27 + x * 28, 17 + y * 29, fill="black")

    def draw_car_vertical(self, canvas, x, y):
        # Car body
        canvas.create_rectangle(x * 28, y * 29, 15 + x * 28, 30 + y * 29, fill="yellow")
        # Car features
        canvas.create_rectangle(x * 28 + 5, y * 29 + 15, 10 + x * 28, 23 + y * 29, fill="black")
        canvas.create_rectangle(x * 28, y * 29, 7 + x * 28, 4 + y * 29, fill="red")
        canvas.create_rectangle(x * 28 + 8, y * 29 , 15 + x * 28, 4 + y * 29, fill="red")
        # 4 wheels
        canvas.create_rectangle(x * 28 - 2, y * 29 + 7, 1 + x * 28, 12 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 - 2, y * 29 + 22, 1 + x * 28, 27 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 + 14, y * 29 + 7, 17 + x * 28, 12 + y * 29, fill="black")
        canvas.create_rectangle(x * 28 + 14, y * 29 + 22, 17 + x * 28, 27 + y * 29, fill="black")

    def draw_dot(self, canvas, x, y):
        canvas.create_rectangle(x * 28 + 12, y * 29 + 12, x * 28 + 16, y * 29 + 16, fill="#fff")

# Testing purpose
if __name__ == "__main__":   
    map = Map()
    map.go()