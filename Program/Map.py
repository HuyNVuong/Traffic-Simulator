from appJar import gui
from Raw import raw_map

# Map class to create a map simulation, map inherit method from GUI class from appJar
# Map __init__ got re-implement to generate a road map right when we initilize a new map
class Map(gui):
    def __init__(self):
        super().__init__("Traffic Simulator", "790x830")
        self.setBg("#ffe4b5")
        wall = self.addCanvas("wall")
        # cars = self.addCanvas("car")
        for y in range(len(raw_map)):
            for x in range(len(raw_map[y])):
                if (raw_map[y][x] == 3):
                    wall.create_oval(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="black", fill="#808080")
                elif(raw_map[y][x] == 2):
                    # Car body
                    wall.create_rectangle(x * 28, y * 29, 30 + x * 28, 15 + y * 29, fill="yellow")
                    # Car features
                    wall.create_rectangle(x * 28 + 15, y * 29 + 5, 23 + x * 28, 10 + y * 29, fill="black")
                    wall.create_rectangle(x * 28, y * 29, 4 + x * 28, 7 + y * 29, fill="red")
                    wall.create_rectangle(x * 28, y * 29 + 8, 4 + x * 28, 15 + y * 29, fill="red")
                    # 4 wells
                    wall.create_rectangle(x * 28 + 7, y * 29 - 2, 12 + x * 28, 1 + y * 29, fill="black")
                    wall.create_rectangle(x * 28 + 22, y * 29 - 2, 27 + x * 28, 1 + y * 29, fill="black")
                    wall.create_rectangle(x * 28 + 7, y * 29 + 14, 12 + x * 28, 17 + y * 29, fill="black")
                    wall.create_rectangle(x * 28 + 22, y * 29 + 14, 27 + x * 28, 17 + y * 29, fill="black")
    
if __name__ == "__main__":   
    map = Map()
    map.go()