from tkinter import Frame, Button, Label, PhotoImage
from time import time
from Map import Map
from Raw import resource_path


class Controller(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='top')
        self._running = False
        self._ispause = False
        self._reset = False
        self.start_time = time()
        self.create_widgets()
        
    def create_widgets(self):
        # Starting Button
        self.start_button = Button(self)
        startImage = PhotoImage(file=resource_path('buttonImages/StartButton.png'))
        smallerImage = startImage.subsample(14,14)
        self.start_button.image = smallerImage
        self.start_button = Button(self, image=smallerImage, command=self.start, height=35, width=75)
        self.start_button.grid(row=2, column=2, columnspan=2, padx=20, pady=10)

        # Pausing Button
        self.pause_button = Button(self)
        pauseImage = PhotoImage(file=resource_path('buttonImages/PauseButton.png'))
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
        stopImage = PhotoImage(file=resource_path('buttonImages/StopButton.png'))
        smallerImage = stopImage.subsample(14,14)
        self.stop_button.image = smallerImage
        self.stop_button = Button(self, image=smallerImage, command=self.stop, height=35, width=75)
        self.stop_button.grid(row=3, column=3, columnspan=2, padx=20, pady=10)

        # Reset Button
        self.reset_button = Button(self)
        resetImage = PhotoImage(file=resource_path('buttonImages/ResetButton.png'))
        smallerImage = resetImage.subsample(14,14)
        self.reset_button.image = smallerImage
        self.reset_button = Button(self, image=smallerImage, command=self.reset, height=35, width=75)
        self.reset_button.grid(row=3, column=7, columnspan=2, padx=200, pady=10)

        # Quit button
        self.quit = Button(self)
        quitImage = PhotoImage(file=resource_path('buttonImages/QuitButton.png'))
        smallerImage = quitImage.subsample(14,14)
        self.quit.image = smallerImage
        self.quit = Button(self, image=smallerImage, command=self.master.destroy, height=35, width=75)
        self.quit.grid(row=3, column=11, columnspan=2, padx=20, pady=10)
        # self.quit.pack(side="right")

    def start(self):
        if self._ispause is False:
            self.start_time = time()
        self._ispause = False
        self._running = True
        self._reset = False
        self.start_timing()
        print("Starting project...")

    def pause(self):
        self._ispause = True
        self._reset = False
        print("Paused.")

    def stop(self):
        self._running = False
        self._ispause = True
        self._reset = False
        print("Stopped.")

    def reset(self):
        self._ispause = True
        self._reset = True
        print("Resetting...") 

    def start_timing(self):
        # your code
        elapsed_time = time() - self.start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        if self._running is True:
            self.timer.configure(text="Time Elapsed : %02d:%02d:%02d"%(hours,minutes,seconds))
            self.after(1000, self.start_timing)
        elif self._running is False:
            self.timer.configure(text="Time Elapsed : %02d:%02d:%02d"%(0,0,0))
            self.after(1000, self.start_timing)

