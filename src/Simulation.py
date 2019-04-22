# Main driver that executes the program

from Map import Map
from Raw import Tiles, Point, resource_path, raw_data
from Car import Car
from Controller import Controller
from tkinter import Tk, Frame, Label, Button, filedialog, Menu, Toplevel, Entry, StringVar
from time import sleep
from PIL import Image, ImageTk
from MapTiles import LightT

# Opening window
class SimulationMenu(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.withdraw()
        self.title('Menu')
        self.iconbitmap(resource_path('./data/traffic.ico'))
        self.create_widgets()
        
        
    def create_widgets(self):
        start_frame = Frame(self, width=850, height=540)
        start_frame.pack()

        raw = Image.open(resource_path('./data/traffic-background.jpg'))
        render = ImageTk.PhotoImage(raw)
        self.background = Label(start_frame, image=render)
        self.background.image = render
        self.background.pack()

        start_label = Label(self.background, text='City Traffic Simulation')
        start_label.grid(row=2, column=3, columnspan=2, padx=300, pady=20)

        start_button = Button(self.background, fg='red', command=self.open_simulation)
        start_button['text'] = 'Open Simulation'
        start_button.grid(row=3, column=3, columnspan=2, padx=300, pady=20)

        row = 4
        for city in raw_data.keys():
            city_btn = Button(self.background, fg='green', text=city,
                        command=lambda city=city:[Map.load_raw_data(raw_data[city]), self.alert_which(city)])
            city_btn.grid(row=row, column=3, columnspan=2, padx=300, pady=20)
            row += 1

        import_button = Button(self.background, fg='green', command=self.openfile)
        import_button['text'] = 'Import Map'
        import_button.grid(row=row, column=3, columnspan=2, padx=300, pady=20)

        creator_button = Button(self.background, fg='blue')
        creator_button['text'] = 'Create a Map'
        creator_button.grid(row=row, column=3, columnspan=2, padx=300, pady=20)

    def alert_which(self, city_name):
        self.title(f'{city_name} loaded !')

    def open_simulation(self):
        self.master.update()
        self.master.deiconify()
        self.destroy()

    def openfile(self) -> str:
        # self.withdraw()
        return filedialog.askopenfilename()

        


class Simulation(Tk):
    def __init__(self):
        super().__init__()
        self.title('Traffic Simulation')
        self.iconbitmap(resource_path('data/traffic.ico'))
        self.pre_sim = SimulationMenu(self)
        self.create_toolbar()
        self.create_widgets()
    
    def create_toolbar(self):
        self.menu = Menu(self)
        self.config(menu=self.menu)
        # File Menu, used for support navigation
        file_menu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Go back to Menu', command=self.open_menu)

        # Edit Menu, used for edting cars and mores
        edit_menu = Menu(self.menu)
        self.menu.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Edit Car Position')
        edit_menu.add_command(label='Edit Car Destination', command=self.edit_car_dest)

    def create_widgets(self):
        self.command = Controller(self)
        self.traffic_map = Map(self)
        car_w_path = {}
        for car in self.traffic_map.get_cars():
            path = self.traffic_map.optimal_path(car)
            car.dx, car.dy = path[1].x - path[0].x, path[1].y - path[0].y
            car.update_state()
            car_w_path[car] = path
        counter = 0
        while self.command._running is not True:
            self.command.update()
            self.update()
        while self.command._running is True:
            if self.command._ispause is not True:
                if counter % 90 == 0:
                    for tl in self.traffic_map.get_traffic_lights():
                        tl.blink()
                    for sl in self.traffic_map.get_sensor_lights():
                        sl.sl_blink()
                if counter % 30 == 0: 
                    for sl in self.traffic_map.get_sensor_lights():
                        found_car = False
                        for car in car_w_path.keys(): 
                            if car.pos in sl.pos.around():
                                found_car = True 
                        if found_car:
                            sl.sl_greenOn() 
                            sl.sl_redOff() 
                        else:
                            sl.sl_greenOff()
                            sl.sl_redOn()    
                    for car, path in car_w_path.items():              
                        if Tiles.stop_sign in car.neighbors():
                            if car.stop_for_three_step():
                                continue
                        update = True
                        for tl in self.traffic_map.get_traffic_lights():
                            if tl.pos in car.pos.neighbors():
                                # print(tl.pos, car.pos.neighbors(), tl.light)
                                if tl.light == LightT.red: # LightT.red 
                                    # print('Red')
                                    car.dx, car.dy = 0, 0
                                    update = False
                                    break
                        if not update:
                            continue
                        if len(path) > 1:
                            car.dx, car.dy = path[1].x - path[0].x, path[1].y - path[0].y
                            car.update_state()
                            path.pop(0)
                        else:
                            car.stop()
                for car in car_w_path.keys():
                    for comp in car.get_component():
                        self.traffic_map.city.move(comp, car.dx, car.dy)
                    if counter % 30 == 0:
                        car.x += car.dx 
                        car.y += car.dy 
                        car.pos = Point(car.x, car.y)
                counter += 1
            sleep(0.01)
            
            self.command.update()
            self.traffic_map.update()
            self.update()

    def edit_car_dest(self):
        window = Toplevel(self)
        display = Label(window, text='Edit Car Destination')
        row = 1
        display.grid(row=1, column=1, columnspan=2, padx=10, pady=20)
        for car in self.traffic_map.get_cars():
            row += 1
            car_label = Label(window, text=f'Car {row - 1}: Pos - {car.dest.pos}, Dest - ')
            car_label.grid(row=row, column=1, columnspan=2, padx=10, pady=20)
            x = StringVar()
            x.set(f'{car.x}')
            x_label = Label(window, text='x : ')
            x_label.grid(row=row, column=3, padx=5, pady=20)
            x_edit = Entry(window, textvariable=x)
            x_edit.grid(row=row, column=4, padx=10, pady=20)
            y = StringVar()
            y.set(f'{car.y}')
            y_label = Label(window, text='y : ')
            y_label.grid(row=row, column=5, padx=5, pady=20)
            y_edit = Entry(window, textvariable=y)
            y_edit.grid(row=row, column=6, padx=10, pady=20)

        

    def open_menu(self):
        self.withdraw()
        self.pre_sim = SimulationMenu(self)

if __name__ == "__main__":
    s = Simulation()
    s.mainloop()