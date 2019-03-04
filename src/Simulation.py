# Main driver that executes the program

from Map import Map
from Raw import *
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk
from time import sleep

if __name__ == "__main__":   
    root = Tk()
    root.title("Traffic Simulator")
    command = CommandPallete(master=root)
    trafficMap = Map(master=root)
    while command.running is True:
        print('moving')
        for car in trafficMap.cars:
            raw_map[car.y][car.x] = Tiles.open_road_down
            car.move()
            raw_map[car.y][car.x] = car.state
            sleep(0.1)
        trafficMap.paint()
        root.update()
    root.mainloop()
    # while command.pause is not True:
    #     root.update()
    
