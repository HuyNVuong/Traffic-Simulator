from Raw import raw_map, Tiles
# import pytest

class SimulationTester(object):
    def pre_test(self):
        # Test that all the entities are there 
        assert Tiles.wall in raw_map
        assert Tiles.road in raw_map
        assert Tiles.car_right in raw_map
        assert Tiles.car_left in raw_map
        assert Tiles.car_down in raw_map
        assert Tiles.car_up in raw_map
        assert Tiles.traffic_lights in raw_map