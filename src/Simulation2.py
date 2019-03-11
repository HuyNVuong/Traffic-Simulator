from tkinter import Tk, Canvas, Frame
from Map import Map
from Car import Car
from Raw import Point, Tiles
from time import sleep
from CommandPallete import CommandPallete

if __name__ == "__main__":
    root = Tk()
    command = CommandPallete(root)
    traffic_map = Map(root)
    car = Car(Point(1, 2), Tiles.car_left, traffic_map)
    # oval = car.create_oval(1, 2, 100, 101, fill="red")
    car.pack()
    while command.running is not True:
        command.update()
        root.update()
    while command.running is True:
        if command._ispause is not True:
            for com in car.get_component():
                car.move(com, 5 , 0)
            sleep(0.1)
        command.update()
        traffic_map.update()
        root.update()
    root.mainloop()