import tkinter as tk
from time import time

class Stopwatch:
    def __init__(self):
        root = tk.Tk()
        root.title('Stopwatch')

        self.display = tk.Label(root, text='00:00', width=20)
        self.display.pack()

        self.button = tk.Button(root, text='Start', command=self.toggle)
        self.button.pack()

        self.paused = True
        root.mainloop()

    def toggle(self):
        if self.paused:
            self.paused = False
            self.button.config(text='Stop')
            self.oldtime = time()
            self.run_timer()
        else:
            self.paused = True
            self.oldtime = time()
            self.button.config(text='Start')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
        self.display.config(text=timestr)
        self.display.after(1000, self.run_timer)

Stopwatch()