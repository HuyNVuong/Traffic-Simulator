from appJar import gui
from Raw import raw_map

# Map class to create a map simulation, map inherit method from GUI class from appJar
# Map __init__ got re-implement to generate a road map right when we initilize a new map
class Map(gui):
    def __init__(self):
        super().__init__("Traffic Simulator", "790x830")
        self.setBg("black")
        wall = self.addCanvas("wall")
        for y in range(len(raw_map)):
            for x in range(len(raw_map[y])):
                if (raw_map[y][x] == 3):
                    wall.create_oval(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="blue")
        wall.create_oval(365, 490, 395, 520, fill="yellow")
    
if __name__ == "__main__":   
    map = Map()
    map.go()