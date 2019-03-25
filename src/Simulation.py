# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map, Point
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
    
    import_button = Button(start_frame, fg="green")
    import_button["text"] = "Import Map"
    import_button.pack()

    creator_button = Button(start_frame, fg="blue")
    creator_button["text"] = "Create a Map"
    creator_button.pack()
    start_window.mainloop() 
    # End of opening window

       

    root = Tk()
    command = CommandPallete(root)
    traffic_map = Map(root)
    counter = 0
    while command.running is not True:
        command.update()
        root.update()
    while command.running is True:
        # for car in traffic_map.get_cars():
        if counter % 90 == 0 and counter > 0:
            for car in traffic_map.get_cars():
                car.turn_left()
                for comp in car.get_component():
                    print(comp)
        if command._ispause is not True:
            for car in traffic_map.get_cars():
                for comp in car.get_component():
                    traffic_map.city.move(comp, car.dx, car.dy)
                car.x += (car.dx / 28) 
                car.y += (car.dy / 29)
        sleep(0.01)
        counter += 1
        command.update()
        traffic_map.update()
        root.update()
        
    root.mainloop()
    # while command.pause is not True:
    #     root.update()
    
