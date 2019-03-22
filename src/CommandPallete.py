from tkinter import Frame, Button, Label, PhotoImage
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
        startImage = PhotoImage(file='buttonImages/StartButton.png')
        smallerImage = startImage.subsample(14,14)
        self.start_button.image = smallerImage
        self.start_button = Button(self, image=smallerImage, command=self.start, height=35, width=75)
        self.start_button.grid(row=2, column=3, columnspan=2, padx=20, pady=10)

        # Pausing Button
        self.pause_button = Button(self)
        pauseImage = PhotoImage(file='buttonImages/PauseButton.png')
        smallerImage = pauseImage.subsample(14,14)
        self.pause_button.image = smallerImage
        self.pause_button = Button(self, image=smallerImage, command=self.pause, height=35, width=75)
        self.pause_button.grid(row=2, column=7, columnspan=2, padx=200, pady=10)

        # Timer label
        self.timer = Label(self)
        self.timer.grid(row=2, column=11, columnspan=2, padx=20, pady=10)
        self.start_timing()

        # Stopping Button
        self.stop_button = Button(self)
        stopImage = PhotoImage(file='buttonImages/StopButton.png')
        smallerImage = stopImage.subsample(14,14)
        self.stop_button.image = smallerImage
        self.stop_button = Button(self, image=smallerImage, command=self.stop, height=35, width=75)
        self.stop_button.grid(row=3, column=3, columnspan=2, padx=20, pady=10)

        # Stepping Button
        self.step_button = Button(self)
        self.step_button["text"] = "Step"
        self.step_button["command"] = self.step
        self.step_button.grid(row=3, column=7, columnspan=2, padx=200, pady=10)

        # Quit button
        self.quit = Button(self)
        quitImage = PhotoImage(file='buttonImages/QuitButton.png')
        smallerImage = quitImage.subsample(14,14)
        self.quit.image = smallerImage
        self.quit = Button(self, image=smallerImage, command=self.master.destroy)
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
