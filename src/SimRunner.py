from Simulation import Simulation
from tkinter import Tk, Canvas, Frame, Button, Label, filedialog
from PIL import Image, ImageTk
from Map import Map
from Raw import resource_path, raw_data
import os 

# Opening window
class SimulationMenu(Tk):
    def __init__(self):
        super().__init__()
        self.title('Menu')
        self.iconbitmap(resource_path('./data/traffic.ico'))
        self.create_widgets()
        
    def create_widgets(self):
        start_frame = Frame(self, width=850, height=540)
        start_frame.pack()

        raw = Image.open('./data/traffic-background.jpg')
        render = ImageTk.PhotoImage(raw)
        self.background = Label(start_frame, image=render, width=850, height=540)
        self.background.image = render
        self.background.pack()

        start_label = Label(self.background, text='City Traffic Simulation')
        start_label.grid(row=2, column=3, columnspan=2, padx=300, pady=20)

        start_button = Button(self.background, fg='red', command=self.destroy)
        start_button['text'] = 'Open Simulation'
        start_button.grid(row=3, column=3, columnspan=2, padx=300, pady=20)

        row = 4
        for i, city in enumerate(raw_data.keys()):
            city_btn = Button(self.background, fg='green', text=city,
                        command=lambda i=i:[Map.load_raw_data(raw_data[city]), self.alert_data_loaded(city)])
            city_btn.grid(row=row, column=3, columnspan=2, padx=300, pady=20)
            row += 1

        import_button = Button(self.background, fg='green', command=self.openfile)
        import_button['text'] = 'Import Map'
        import_button.grid(row=row, column=3, columnspan=2, padx=300, pady=20)

        creator_button = Button(self.background, fg='blue')
        creator_button['text'] = 'Create a Map'
        creator_button.grid(row=row, column=3, columnspan=2, padx=300, pady=20)

    def alert_data_loaded(self, city_name):
        self.title(f'{city_name} loaded !')

    def openfile(self) -> str:
        # self.withdraw()
        return filedialog.askopenfilename()

        

def main():
    menu = SimulationMenu()
    menu.mainloop()
    runner = Simulation()
    if runner.command._reset:
        runner = Simulation()
    runner.mainloop()

if __name__ == "__main__":
    main()