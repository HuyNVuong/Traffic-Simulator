from tkinter import Canvas 
from Raw import Point, Tiles

class MapTiles(Canvas):
    def __init__(self, coordinate : Point, state, master=None):
        super().__init__(master=master)
        self.master = master
        self.state = state 
        self.x = coordinate.x
        self.y = coordinate.y
        if state == Tiles.stop_sign:
            self.draw_stop_sign()

    def __repr__(self):
        return 'Tiles'

    def draw_stop_sign(self):
        points = [[self.x * 30, self.y * 30 + 8],[self.x * 30 + 8, self.y * 30],[self.x * 30 + 16, self.y * 30],
                  [self.x * 30 + 24, self.y * 30 + 8],[self.x * 30 + 24, self.y * 30 + 16], 
                  [self.x * 30 + 16, self.y * 30 + 24],[self.x * 30 + 8, self.y * 30 + 24], [self.x * 30, self.y * 30 + 16]]
        self.master.city.create_polygon(points, fill = "red")
        self.master.city.create_text((self.x * 30 + 10, self.y * 30 + 10), text="STOP")


    def draw_traffic_lights(self):
        self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill = "grey")
        self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill = "grey")
        self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill = "grey")

    
    
    #Traffic light change functions
    def redOn(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="red")
            tk.update()
            time.sleep(0.05)

    def redOff(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            red = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            tk.update()
            time.sleep(0.05)

    def yellowOn(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="yellow")
            tk.update()
            time.sleep(0.05)

    def yellowOff(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            yellow = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            tk.update()
            time.sleep(0.05)

    def greenOn(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="green")
            tk.update()
            time.sleep(0.05)

    def greenOff(sec):
        t_end = time.time() + sec
        while time.time() < t_end:
            green = self.master.city.create_oval(self.x * 30, self.y * 30 + 8, self.x * 30 + 16, self.y * 30 + 16, fill="grey")
            tk.update()
            time.sleep(0.05)
