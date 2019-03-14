from tkinter import Frame, Button, Label
from time import time
from Map import Map

class CommandPallete(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.start_time = time()
        self.pack(side='top')
        self.running = False
        self.create_widgets()
        self._ispause = False
        
    def create_widgets(self):
        # Starting Button
        self.start_button = Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start
        self.start_button.grid(row=2, column=3, columnspan=2, padx=20, pady=10)

        # Pausing Button
        self.pause_button = Button(self)
        self.pause_button["text"] = "Pause"
        self.pause_button["command"] = self.pause
        self.pause_button.grid(row=2, column=7, columnspan=2, padx=200, pady=10)

        # Timer label
        self.timer = Label(self)
        self.timer.grid(row=2, column=11, columnspan=2, padx=20, pady=10)
        self.start_timing()

        # Stopping Button
        self.stop_button = Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop
        self.stop_button.grid(row=3, column=3, columnspan=2, padx=20, pady=10)

        # Stepping Button
        self.step_button = Button(self)
        self.step_button["text"] = "Step"
        self.step_button["command"] = self.step
        self.step_button.grid(row=3, column=7, columnspan=2, padx=200, pady=10)

        # Quit button
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row=3, column=11, columnspan=2, padx=20, pady=10)
        # self.quit.pack(side="right")

    def start(self):
        self._ispause = False
        self.running = True
        print("Starting project...")

    def pause(self):
        self._ispause = True
        print("Paused.")

    def stop(self):
        self.running = False
        print("Stopped.")

    def step(self):
        for car in Map.cars:
            car.move()

    def start_timing(self):
        # your code
        elapsed_time = time() - self.start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        self.timer.configure(text="Time Elapsed : %02d:%02d:%02d"%(hours,minutes,seconds))
        self.after(1000, self.start_timing)
