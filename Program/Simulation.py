# Main driver that executes the program

from Map import Map
from Raw import Point, Unit, Turn
from Car import Car

if __name__ == "__main__":   
    map = Map()
    car = Car(Point(6, 16), 0, 1)
    map.add_car(car)
    map.go()
    
    