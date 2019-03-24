from tkinter import Frame, Canvas, Tk
from typing import List
from Car import Car
from Raw import Point, raw_map, Tiles
from ActionListener import actionListenter

# Map class to create a map simulation, map inherit method from GUI class from appJar
# Map __init__ got re-implement to generate a road map right when we initilize a new map


class Map(Frame):
	def __init__(self, master=None):
		super().__init__(master, width=850, height=540)
		self.master = master 
		self.pack(side='bottom')
		self.create_widgets()
		
	__cars = set()

	def create_widgets(self):
		self.city = Canvas(self, width=850, height=480)
		self.paint()
		self.city.pack()

	def paint(self):
		for y in range(len(raw_map)):
			for x in range(len(raw_map[y])):
				if raw_map[y][x] == Tiles.wall:    
					self.city.create_rectangle(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="black", fill="#808080")
				elif raw_map[y][x] == Tiles.car_left:
					car = Car(Point(x, y), raw_map[y][x], self.city)
					self.__cars.add(car)

	def say_hi(self):
		print("hi there, everyone!")
		
	def draw_block(self, x, y):
		self.city.create_rectangle(x * 28, y * 29, 20 + x * 28, 20 + y * 29, outline="black", fill="#808080")

	def draw_dot(self, x, y):
		self.city.create_rectangle(x * 28 + 10, y * 29 + 10, x * 28 + 16, y * 29 + 16, fill="#fff")

	def add_car(self, x, y, state):
		car = Car(Point(x, y), state, self.city)
		self.__cars.add(car)

	def get_cars(self) -> set():
		return self.__cars

	def open_spot(self):
		open_spot = []
		for y, row in enumerate(raw_map):
			for x, spot in enumerate(row):
				if spot == 0:
					open_spot.append(Point(x, y))
		return open_spot



