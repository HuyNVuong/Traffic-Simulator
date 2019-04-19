from Raw import raw_data, Tiles, predef, Point
import pytest
from Car import Car
from Map import Map
from MapTiles import MapTiles

raw_map = raw_data['City 1']
# class SimulationTester():
def test_raw_map_data():
    '''
    Asserting if all the tiles are inside the map
    Ex:
    >>> Tiles.wall in raw_map
    True
    '''
    assert Tiles.wall in raw_map
    assert Tiles.road in raw_map
    assert Tiles.car_right in raw_map
    assert Tiles.car_left in raw_map
    assert Tiles.car_down in raw_map
    assert Tiles.car_up in raw_map
    assert Tiles.traffic_lights in raw_map

def test_raw_entities():
    '''
    Asserting if enumerated types are equal to the predefined types
    Ex:
    >>> Tiles.wall
    <Tiles.wall: 0>
    >>> predef['wall']
    0
    >>> Tiles.wall == predef['wall']
    True
    '''
    assert Tiles.wall == predef['wall']
    assert Tiles.road == predef['road']
    assert Tiles.stop_sign == predef['stop_sign']
    assert Tiles.traffic_lights == predef['traffic_lights']
    assert Tiles.intersection == predef['intersection']
    assert Tiles.car_up == predef['car_up']
    assert Tiles.car_down == predef['car_down']
    assert Tiles.car_left == predef['car_left']
    assert Tiles.car_right == predef['car_right']

def test_car_creation():
    car = Car(Point(5, 7), Tiles.car_left)
    assert car.master is None
    assert car.dx == -1
    assert car.dy == 0
    assert car.color == "yellow"
    assert car.dest == None

    car1 = Car(Point(5,8), Tiles.car_left, dest=Point(7,8), body="green")
    assert car1.master is None
    assert car1.dx == -1
    assert car1.dy == 0
    assert car1.color == "green" #TODO figure out how to change color
    assert car1.dest == Point(7,8)

def test_short_path():
    m = Map()
    car = Car(Point(5, 8), Tiles.car_left, master=m.city, dest=Point(8,8))
    expected_path1 = [Point(5,8), Point(6,8), Point(7, 8), Point(8,8)]
    m.optimal_path(car)
    assert expected_path1 == m.optimal_path(car)


    car.pos = Point(6,8)
    car.dest = Point(4,6)
    expected_path2 = None
    assert expected_path2 is None

    car.pos = Point(5,8)
    car.dest = Point(3,6)
    car.state = Tiles.car_left
    expected_path3 = [Point(5,8), Point(4,8), Point(3,8), Point(3,7), Point(3,6)]
    m.optimal_path(car)
    assert expected_path3 == m.optimal_path(car)

def test_turning():
    '''
    Asserting if a car object turns left and updates its state correctly 
    >>> car = Car(Point(5,8), Tiles.car_left)
    >>> car.turn_left()
    >>> car.state 
    <Tiles.car_down: 6>
    '''
    car = Car(Point(5,8), Tiles.car_left)
    car.turn_left()
    assert car.dx == 0
    assert car.dy == 1
    assert car.state == Tiles.car_down
    assert car.pos == Point(5,8)

    car.turn_right()
    assert car.dx == -1
    assert car.dy == 0
    assert car.state == Tiles.car_left
    assert car.pos == Point(5,8)

    car.turn_right()
    assert car.dx == 0
    assert car.dy == -1
    assert car.state == Tiles.car_up
    assert car.pos == Point(5,8)

    car.turn_left()
    car.turn_left()
    car.turn_left()
    assert car.dx == 1
    assert car.dy == 0
    assert car.state == Tiles.car_right
    assert car.pos == Point(5,8)

def test_update_state():
    car = Car(Point(5,8), Tiles.car_left)
    car.state = Tiles.car_right
    car.update_speed()
    # car.update_state()
    assert car.state == Tiles.car_right
    assert car.dx == 1
    assert car.dy == 0

