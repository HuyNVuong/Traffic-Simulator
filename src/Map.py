from tkinter import Frame, Canvas, Tk
from typing import List # Optional
from Car import Car
from Raw import Point, raw_map, Tiles
from MapTiles import MapTiles
from enum import Enum
import heapq
import random

colors = ["orange", "yellow", "green", "blue", "indigo", "violet"]

class Map(Frame):

	__cars = set()
	__traffic_lights = set()
	__walls = set()
	__open_spot = {Point(x, y)
		for y, row in enumerate(raw_map)
			for x, spot in enumerate(row) if spot == 1}

	def __init__(self, master=None):
		super().__init__(master, width=900, height=540)
		self.master = master 
		self.pack(side='bottom')
		self.create_widgets()

	def create_widgets(self):
		self.city = Canvas(self, width=900, height=480)
		self.paint()
		self.city.pack()

	def paint(self):
		for y in range(len(raw_map)):
			for x in range(len(raw_map[y])):
				if raw_map[y][x] == Tiles.wall:    
					self.city.create_rectangle(x * 30, y * 30, 20 + x * 30, 20 + y * 30, outline="black", fill="#808080")
					self._Map__walls.add(Point(x, y))

				elif raw_map[y][x] == Tiles.car_left or raw_map[y][x] == Tiles.car_down \
					or raw_map[y][x] == Tiles.car_right or raw_map[y][x] == Tiles.car_up:
					color = random.choice(colors)
					car = Car(Point(x, y), raw_map[y][x], self.city, color, body=color)
					car_dest = random.sample(self._Map__open_spot, 1)[0]
					self.city.create_arc(car_dest.x * 30 + 1, car_dest.y * 30 + 40, car_dest.x * 30 + 20, car_dest.y * 30, start=0, extent=180, fill=color)
					self.city.create_text((car_dest.x * 30 + 12, car_dest.y * 30 + 11), text="A", fill="white")
					self._Map__open_spot.remove(car_dest)
					car.dest = car_dest
					self.__cars.add(car)

				elif raw_map[y][x] == Tiles.stop_sign:
					MapTiles(Point(x, y), raw_map[y][x], self)
					
				elif raw_map[y][x] == Tiles.traffic_lights:
					tl = MapTiles(Point(x, y), raw_map[y][x], self)
					if (raw_map[y][x + 1] == Tiles.road and raw_map[y + 1][x] == Tiles.road) \
						or (raw_map[y - 1][x] == Tiles.road and raw_map[y][x - 1] == Tiles.road):
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
	it uses a method of breath first search (BFS)

	>>> optimal_path(car, Point(3, 4), Tiles.car_up, dest=Point(5, 7))
	[Point(3, 4), Point(3, 5), Point(3, 6), Point(3, 7), Point(4, 7), Point(5, 7)]

	Return None if the dest is occupied or unreachable by the car
	>>> optimal_path(car, Point(3, 4), Tiles.car_up, dest=Point(10, 0))
	None
	'''
	def optimal_path(self, car : Car): # -> Optional[List[Point]]
		# If destination is not specified
		if car.dest is None:
			return None

		# Occupied spaces, or visited vertex
		off_limits = self._Map__walls | ( {c.pos for c in self._Map__cars} ^ {car.pos} ) 

		# Fancier way to do this : we stop at the point before the beacon
		# targets = set() 
		# if car.dest not in off_limits:
		# 	targets = {p for p in car.dest.neighbors() if p not in off_limits} 
		# else:
		# 	return None

		result = []
		best = None 
		queue = [(0, [car.pos])] # Start with car starting position
		while queue: 
			distance, path = heapq.heappop(queue)
			if best and len(path) > best:
				return result[0]
			node = path[-1] # -> pop off last element of path
			if node == car.dest:
				result.append(path)
				best = len(path)
			if node in off_limits:
				continue
			off_limits.add(node)
			for neig in node.neighbors():
				if neig in off_limits:
					continue
				heapq.heappush(queue, (distance + 1, path + [neig]))
		return result[0]

	



