# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map, Point, resource_path
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk, Frame, Label, Button
from time import sleep
from PIL import Image, ImageTk

if __name__ == '__main__':  

    # Opening window
    start_window = Tk()
    start_window.title('Menu')
    start_frame = Frame(start_window, width=850, height=540)
    start_frame.pack()

    raw = Image.open(resource_path('data/traffic-background.jpg'))
    render = ImageTk.PhotoImage(raw)
    img = Label(start_frame, image=render, width=850, height=540)
    img.image = render
    img.pack()

    start_label = Label(img, text='City Traffic Simulation')
    start_label.grid(row=2, column=3, columnspan=2, padx=300, pady=20)

    start_button = Button(img, fg='red', command=start_window.destroy)
    start_button['text'] = 'Open Simulation'
    start_button.grid(row=3, column=3, columnspan=2, padx=300, pady=20)

    import_button = Button(img, fg='green')
    import_button['text'] = 'Import Map'
    import_button.grid(row=4, column=3, columnspan=2, padx=300, pady=20)

    creator_button = Button(img, fg='blue')
    creator_button['text'] = 'Create a Map'
    creator_button.grid(row=5, column=3, columnspan=2, padx=300, pady=20)

    start_window.mainloop() 
    # End of opening window

    root = Tk()
    root.title('Traffic Simulation')
    command = CommandPallete(root)
    traffic_map = Map(root)
    car_tmp = Car(Point(3, 4), Tiles.car_up, master=traffic_map.city)
    counter = 0
    while command._running is not True:
        command.update()
        root.update()
    while command._running is True:
        ## Hardcode optimal path for a car
        if counter == 60: car_tmp.turn_right()
        if counter == 180: car_tmp.turn_right()
        if counter == 360: car_tmp.turn_left()
        if counter == 810: car_tmp.turn_right()
        if counter == 960: car_tmp.turn_left()
        if counter == 1110: car_tmp.turn_right()
        if counter == 1140: 
            car_tmp.turn_left()
            car_tmp.stop()

        if counter % 150 == 0 and counter > 0:
            for car in traffic_map.get_cars():
                car.turn_right()
        if command._ispause is not True:
            for car in traffic_map.get_cars():
                for comp in car.get_component():
                    traffic_map.city.move(comp, car.dx, car.dy)
                car.x += (car.dx / 30) 
                car.y += (car.dy / 30)
            # Preprogrammed
            for comp_tmp in car_tmp.get_component():
                traffic_map.city.move(comp_tmp, car_tmp.dx, car_tmp.dy)
            car_tmp.x += (car_tmp.dx / 30) 
            car_tmp.y += (car_tmp.dy / 30) 
            counter += 1
        sleep(0.01)
        
        command.update()
        traffic_map.update()
        root.update()
        
    root.mainloop()
    # while command.pause is not True:
    #     root.update()
    
