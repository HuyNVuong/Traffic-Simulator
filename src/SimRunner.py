from Simulation import Simulation
from tkinter import Tk, Canvas, Frame, Button, Label, filedialog
from PIL import Image, ImageTk

 # Opening window
class SimulationMenu(Tk):
    def __init__(self):
        super().__init__()
        self.title('Menu')
        self.iconbitmap('C:\\Users\\vuong\\Documents\\CSCE\\cse361\\csce_361\\src\\data\\traffic.ico')
        self.create_widgets()
        
    def create_widgets(self):
        start_frame = Frame(self, width=850, height=540)
        start_frame.pack()

        raw = Image.open('./data/traffic-background.jpg')
        render = ImageTk.PhotoImage(raw)
        self.img = Label(start_frame, image=render, width=850, height=540)
        self.img.image = render
        self.img.pack()

        start_label = Label(self.img, text='City Traffic Simulation')
        start_label.grid(row=2, column=3, columnspan=2, padx=300, pady=20)

        start_button = Button(self.img, fg='red', command=self.destroy)
        start_button['text'] = 'Open Simulation'
        start_button.grid(row=3, column=3, columnspan=2, padx=300, pady=20)

        import_button = Button(self.img, fg='green', command=self.openfile)
        import_button['text'] = 'Import Map'
        import_button.grid(row=4, column=3, columnspan=2, padx=300, pady=20)

        creator_button = Button(self.img, fg='blue')
        creator_button['text'] = 'Create a Map'
        creator_button.grid(row=5, column=3, columnspan=2, padx=300, pady=20)

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