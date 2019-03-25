# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map, Point
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk, Frame, Label, Button
from time import sleep
from PIL import Image, ImageTk

if __name__ == "__main__":  

    # Opening window
    start_window = Tk()
    start_window.title("Menu")
    start_frame = Frame(start_window, width=850, height=540, bg='#d6a44a')
    start_frame.pack()

    # raw = Image.open('./data/traffic-background.jpg')
    # render = ImageTk.PhotoImage(raw)
    # img = Label(start_frame, image=render, width=850, height=540)
    # img.image = render
    # img.pack()

    start_label = Label(start_frame, text="City Traffic Simulation")
    start_label.grid(row=2, column=3, columnspan=2, padx=300, pady=20)

    start_button = Button(start_frame, fg="red", command=start_window.destroy)
    start_button["text"] = "Open Simulation"
    start_button.grid(row=3, column=3, columnspan=2, padx=300, pady=20)

    import_button = Button(start_frame, fg="green")
    import_button["text"] = "Import Map"
    import_button.grid(row=4, column=3, columnspan=2, padx=300, pady=20)

    creator_button = Button(start_frame, fg="blue")
    creator_button["text"] = "Create a Map"
    creator_button.grid(row=5, column=3, columnspan=2, padx=300, pady=20)

    start_window.mainloop() 
    # End of opening window

       

    root = Tk()
    root.title("Traffic Simulation")
    command = CommandPallete(root)
    traffic_map = Map(root)
    counter = 0
    while command.running is not True:
        command.update()
        root.update()
    while command.running is True:
        # for car in traffic_map.get_cars():
        if counter % 150 == 0 and counter > 0:
            for car in traffic_map.get_cars():
                car.turn_left()
        if command._ispause is not True:
            for car in traffic_map.get_cars():
                for comp in car.get_component():
                    traffic_map.city.move(comp, car.dx, car.dy)
                car.x += (car.dx / 30) 
                car.y += (car.dy / 30)
        sleep(0.01)
        counter += 1
        command.update()
        traffic_map.update()
        root.update()
        
    root.mainloop()
    # while command.pause is not True:
    #     root.update()
    
