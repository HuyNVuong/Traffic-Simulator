from Raw import raw_map, Tiles, predef
import pytest

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


