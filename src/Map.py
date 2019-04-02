from tkinter import Frame, Canvas, Tk
from typing import List # Optional
from Car import Car
from Raw import Point, raw_map, Tiles
from MapTiles import MapTiles
from enum import Enum

class Map(Frame):
	def __init__(self, master=None):
		super().__init__(master, width=900, height=540)
		self.master = master 
		self.pack(side='bottom')
		self.create_widgets()
		
	__cars = set()
	__traffic_lights = set()

	def create_widgets(self):
		self.city = Canvas(self, width=900, height=480)
		self.paint()
		self.city.pack()

	def paint(self):
		for y in range(len(raw_map)):
			for x in range(len(raw_map[y])):
				if raw_map[y][x] == Tiles.wall:    
					self.city.create_rectangle(x * 30, y * 30, 20 + x * 30, 20 + y * 30, outline="black", fill="#808080")
				elif raw_map[y][x] == Tiles.car_left or raw_map[y][x] == Tiles.car_down:
					car = Car(Point(x, y), raw_map[y][x], self.city)
					self.__cars.add(car)
				elif raw_map[y][x] == Tiles.stop_sign:
					MapTiles(Point(x, y), raw_map[y][x], self)
				elif raw_map[y][x] == Tiles.traffic_lights:
					tl = MapTiles(Point(x, y), raw_map[y][x], self)
					if (raw_map[y][x + 1] == Tiles.road and raw_map[y + 1][x] == Tiles.road) or (raw_map[y - 1][x] == Tiles.road and raw_map[y][x - 1] == Tiles.road):
						tl.redOn() 
					else: 
						tl.greenOn()
					self.__traffic_lights.add(tl)
		
	def draw_block(self, x, y, designated=False):
		self.city.create_rectangle(x * 30, y * 30, 30 + x * 30, 30 + y * 30, outline="black", fill="#808080")

	def draw_dot(self, x, y):
		self.city.create_rectangle(x * 30 + 10, y * 30 + 10, x * 30 + 16, y * 30 + 16, fill="#fff")

	def add_car(self, x, y, state):
		car = Car(Point(x, y), state, self.city)
		self.__cars.add(car)

	def get_cars(self) -> set():
		return self._Map__cars

	def get_traffic_lights(self) -> set():
		return self.__traffic_lights

	''' 
	This function returns an {maybe} optimal path of a car from 
	point A to point B
	>>> optimal_path(car)
	'''
	def optimal_path(self, car : Car): # -> Optionnal[List[Point]]
		pass

	def open_spot(self):
		open_spot = []
		for y, row in enumerate(raw_map):
			for x, spot in enumerate(row):
				if spot == 0:
					open_spot.append(Point(x, y))
		return open_spot



