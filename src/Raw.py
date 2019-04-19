from enum import IntEnum
from typing import NamedTuple, List
from numpy import zeros, array
import os
import sys

class Point(NamedTuple):
    x : int
    y : int

    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    def neighbors(self):
        x, y = self.x, self.y 
        return {Point(x - 1, y), Point(x + 1, y), 
                    Point (x, y - 1), Point(x, y + 1)}

    def around(self):
        x, y = self.x, self.y 
        return {Point(x - 1, y - 1), Point(x, y - 1), Point(x + 1, y - 1),
                Point(x - 1, y), Point(x, y), Point(x + 1, y),
                Point(x - 1, y + 1), Point(x, y + 1), Point(x + 1, y + 1) }

    def manhattan(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

class Tiles(IntEnum):
    wall = 0
    road = 1
    stop_sign = 2
    traffic_lights = 3
    intersection = 4
    car_up = 5
    car_down = 6
    car_left = 7
    car_right = 8
    sensor_light = 9

predef = {
    "wall" : 0,
    "road" : 1,
    "stop_sign" : 2,
    "traffic_lights" : 3,
    "intersection" : 4,
    "car_up" : 5,
    "car_down" : 6,
    "car_left" : 7,
    "car_right" : 8,
    "sensor_light" : 9
}

def resource_path(relative_path) -> str: 
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', '.')+'/'
    except Exception:
        base_path = os.path.abspath(".")

    return base_path + relative_path

# Initial map for adhoc testing
raw_data = { 'City 1' : array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 9, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 1, 1, 8, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 7, 1, 1, 4, 4, 0, 0, 0, 4, 4, 0],
                               [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 5, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 6, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 8, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),

             'City 2' : array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 9, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 1, 1, 8, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0, 0, 0, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 7, 1, 1, 4, 4, 0, 0, 0, 4, 4, 0],
                               [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 5, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 6, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                               [0, 0, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 1, 1, 1, 1, 8, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
            }

def fromCSV(file_path : str):
    with open(file_path) as file:
        raw_data = []
        for line in file:
            row = []
            for e in line.strip().split(','):
                row.append( predef[e.lower()])
            raw_data.append(row)
    return array(raw_data)

def toCSV(data : List[List[int]]) -> bool:
    return False

