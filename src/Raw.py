from enum import IntEnum
from typing import NamedTuple, List
from numpy import zeros, array
import os
import sys

class Point(NamedTuple):
    x : int
    y : int

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

predef = {
    "wall" : 0,
    "road" : 1,
    "stop_sign" : 2,
    "traffic_lights" : 3,
    "intersection" : 4,
    "car_up" : 5,
    "car_down" : 6,
    "car_left" : 7,
    "car_right" : 8
}

def resource_path(relative_path) -> str: 
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', '.')+'/'
    except Exception:
        base_path = os.path.abspath(".")

    return base_path + relative_path

def fromCSV(file_path : str):
    with open(file_path) as file:
        raw_data = [line.strip().split(',') for line in file]
    return array(raw_data)

def toCSV(data : List[List[int]]) -> bool:
    return False

# Initial map for adhoc testing
raw_map =  array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 0, 3, 1, 1, 3, 0, 3, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 5, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 6, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])       

        




