# Main driver that executes the program

from Map import Map
from Raw import Point, Unit
from Car import Car

if __name__ == "__main__":   
    map = Map()
    car = Car(Point(6, 16), 0, 1, Unit.horizontal_car)
    map.add_car(car)
    map.go()
    