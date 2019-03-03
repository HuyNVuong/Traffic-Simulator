# Main driver that executes the program

from Map import Map
from Raw import *
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk

if __name__ == "__main__":   
    root = Tk()
    root.title("Traffic Simulator")
    command = CommandPallete(master=root)
    trafficMap = Map(master=root)
    # while command.pause is not True:
    #     root.update()
    root.mainloop()
