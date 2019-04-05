# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map, Point, resource_path
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk, Frame, Label, Button
from time import sleep
from PIL import Image, ImageTk

class Simulation(Tk):
    def __init__(self):
        super().__init__()
        self.title('Traffic Simulation')
        self.iconbitmap(resource_path('data/traffic.ico'))
        self.create_widgets()
    
    def create_widgets(self):
        self.command = CommandPallete(self)
        self.traffic_map = Map(self)
        # car_tmp = Car(Point(5, 7), Tiles.car_left, master=self.traffic_map.city, dest=Point(27, 14))
        # print(self.traffic_map.optimal_path(car_tmp))
        car_w_path = {}
        for car in self.traffic_map.get_cars():
            path = self.traffic_map.optimal_path(car)
            car.dx, car.dy = path[1].x - path[0].x, path[1].y - path[0].y
            car.update_state()
            car_w_path[car] = path
            # print(car, path)
        counter = 0
        while self.command._running is not True:
            self.command.update()
            self.update()
        while self.command._running is True:
            if self.command._ispause is not True:
                if counter % 90 == 0:
                    for tl in self.traffic_map.get_traffic_lights():
                        tl.blink()
                if counter % 30 == 0: 
                    for car, path in car_w_path.items():
                        if len(path) > 1:
                            car.dx, car.dy = path[1].x - path[0].x, path[1].y - path[0].y
                            car.update_state()
                            path.pop(0)
                        else:
                            car.stop()
                for car in car_w_path.keys():
                    # for head in car.head():
                        # print(head, raw_map[int(head.y)][int(head.x)])
                        # if raw_map[int(head.y)][int(head.x)] == Tiles.stop_sign:
                        #     car.dx, car.dy = 0, 0
                    for comp in car.get_component():
                        self.traffic_map.city.move(comp, car.dx, car.dy)
                    if counter % 30 == 0:
                        car.x += car.dx 
                        car.y += car.dy 
                counter += 1
            sleep(0.01)
            
            self.command.update()
            self.traffic_map.update()
            self.update()


