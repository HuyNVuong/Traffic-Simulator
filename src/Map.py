from tkinter import Frame, Canvas, Tk
from typing import List # Optional
from Car import Car
from Raw import Point, Tiles, fromCSV, raw_data
from MapTiles import MapTiles
from enum import Enum
import heapq
import random

colors 		   = ['#C7980A', '#F4651F', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
block_colors_0 = ['#498B62', '#369058', '#1FD464', '#137D3B']
block_colors_1 = ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
block_colors   = [block_colors_0, block_colors_1]


class Map(Frame):

	__cars = set()
	__traffic_lights = set()
	__walls = set()
	__sensor_lights = set()
	__raw_map = []
	__open_spots = set()

	def __init__(self, master=None):
		super().__init__(master, width=900, height=540)
		self.master = master 
		self.pack(side='bottom')
		self.sprites = random.choice(block_colors)
		# print(self._Map__raw_map)
		self.create_widgets()

	def create_widgets(self):
		if not len(self.__raw_map):
			print('No map loaded, getting default map')
			self._Map__raw_map = raw_data['City 1']
			self._Map__open_spots =  \
						{Point(x, y)
							for y, row in enumerate(self._Map__raw_map)
								for x, spot in enumerate(row) 
									if (spot == Tiles.road or spot == Tiles.intersection)}
		print(self._Map__raw_map)
		self.city = Canvas(self, width=900, height=480)
		self.city.data = self._Map__raw_map
		self.paint()
		self.city.pack()

	@staticmethod
	def load_raw_data(data : List[List[int]]):
		Map.__raw_map = data
		Map.__open_spots = \
				{Point(x, y)
					for y, row in enumerate(Map.__raw_map)
						for x, spot in enumerate(row) 
							if (spot == Tiles.road or spot == Tiles.intersection)}		

	@staticmethod
	def get_raw_map() -> List[List[int]]:
		return Map._Map__raw_map
		
	def paint(self):
		# self.self._Map__raw_map = fromCSV('./data/Map01.csv')
		for y in range(len(self._Map__raw_map)):
			for x in range(len(self._Map__raw_map[y])):
				if self._Map__raw_map[y][x] == Tiles.wall:    
					self.city.create_rectangle(x * 30, y * 30, 20 + x * 30, 20 + y * 30, outline="black", fill=random.choice(self.sprites))
					self._Map__walls.add(Point(x, y))

				elif self._Map__raw_map[y][x] == Tiles.car_left or self._Map__raw_map[y][x] == Tiles.car_down \
					or self._Map__raw_map[y][x] == Tiles.car_right or self._Map__raw_map[y][x] == Tiles.car_up:
						color = random.choice(colors)
						colors.remove(color)
						car_dest = random.sample(self._Map__open_spots, 1)[0]
						car = Car(Point(x, y), self._Map__raw_map[y][x], master=self.city, dest=car_dest, body=color)
						self.add_car(car)

				elif self._Map__raw_map[y][x] == Tiles.stop_sign:
					MapTiles(Point(x, y), self._Map__raw_map[y][x], self.city)
					
				elif self._Map__raw_map[y][x] == Tiles.traffic_lights:
					tl = MapTiles(Point(x, y), self._Map__raw_map[y][x], self.city)
					if (self._Map__raw_map[y][x + 1] == Tiles.road and self._Map__raw_map[y + 1][x] == Tiles.road) \
						or (self._Map__raw_map[y - 1][x] == Tiles.road and self._Map__raw_map[y][x - 1] == Tiles.road):
						tl.redOn() 
					else: 
						tl.greenOn()
					self.__traffic_lights.add(tl)
		
				elif self._Map__raw_map[y][x] == Tiles.sensor_light:
					sl = MapTiles(Point(x, y), self._Map__raw_map[y][x], self.city)
					self._Map__sensor_lights.add(sl)


	def draw_block(self, x, y, designated=False):
		self.city.create_rectangle(x * 30, y * 30, 30 + x * 30, 30 + y * 30, outline="black", fill="#808080")

	def draw_dot(self, x, y):
		self.city.create_rectangle(x * 30 + 10, y * 30 + 10, x * 30 + 16, y * 30 + 16, fill="#fff")

	def add_car(self, car):
		self._Map__open_spots.remove(car.dest)
		self.city.create_arc(car.dest.x * 30 + 1, car.dest.y * 30 + 40, car.dest.x * 30 + 20, car.dest.y * 30, start=0, extent=180, fill=car.color)
		self.city.create_text((car.dest.x * 30 + 12, car.dest.y * 30 + 11), text="A", fill="white")
		self.__cars.add(car)
		if Point(car.dx, car.dy) in self._Map__open_spots:
			self._Map__open_spots.remove(Point(car.x, car.y))

	def get_cars(self) -> set():
		return self._Map__cars

	def get_traffic_lights(self) -> set():
		return self._Map__traffic_lights

	def get_sensor_lights(self) -> set():
		return self._Map__sensor_lights

	def get_open_spots(self):
		return self._Map__open_spots

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
		stop_signs = {Point(x, y)
						for y, row in enumerate(self._Map__raw_map)
							for x, spot in enumerate(row) if spot == Tiles.stop_sign}

		off_limits = (self._Map__walls | {t.pos for t in self._Map__traffic_lights} | \
						 {c.pos for c in self._Map__cars} | stop_signs | self._Map__sensor_lights)

		if car.pos in off_limits:
			off_limits.remove(car.pos)
		
		if car.dest in off_limits:
			return None

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

	

	



