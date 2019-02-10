# Main driver that executes the program

from Map import Map
from Raw import Point, Unit, Turn
from Car import Car

if __name__ == "__main__":   
    map = Map()
    map.add_car(Car(Point(6, 16), 3))
    map.add_car(Car(Point(26, 27), 4))
    map.paint()
    map.go()
    
