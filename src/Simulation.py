# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk, Frame, Label, Button
from time import sleep

if __name__ == "__main__":  

    # Opening window
    start_window = Tk()
    start_frame = Frame(start_window)
    start_frame.pack()
    start_label = Label(start_frame, text="MAYOR ONLY")
    start_label.pack()
    start_button = Button(start_frame, fg="red", command=start_window.destroy)
    start_button["text"] = "Open Simulation"
    start_button.pack()
    start_window.mainloop() 
    # End of opening window



    root = Tk()
    root.title("Traffic Simulator")
    command = CommandPallete(master=root)
    trafficMap = Map(master=root)
    while command.running is True:
        print('moving')
        for car in trafficMap.cars:
            raw_map[car.y][car.x] = Tiles.open_road_down
            car.move()
            raw_map[car.y][car.x] = car.state
            sleep(0.1)
        trafficMap.paint()
        root.update()
    root.mainloop()
    # while command.pause is not True:
    #     root.update()
    
