import tkinter as tk
from time import time

class Signs:
    def __init__(self):
        root = tk.Tk()
        root.title('Signs')


        self.button = tk.Button(root, text='Select Your Desire', command=self.desiredSigns)
        self.button.grid(row=2, column=3, columnspan=2, padx=20, pady=10)
        self.button.pack()
        self.otherbutton = tk.Button(root, text='Select Your Desire', command=self.desiredSign)
        self.otherbutton.grid(row=2, column=7, columnspan=2, padx=200, pady=10)
        self.otherbutton.pack()
        self.button2 = tk.Button(root, text='Select Your Desire', command=self.desired)
        self.button2.pack()
        self.otherbutton2 = tk.Button(root, text='Select Your Desire', command=self.desiredSign2)
        self.otherbutton2.pack()




        self._ispaused = True
        root.mainloop()

    def desiredSigns(self):
        if self._ispaused:
            self._ispaused = False
            self.button.config(text='Stop Sign')
        else:
            self._ispaused = True
            self.button.config(text='Traffic Light')
            
    def desiredSign(self):
        if self._ispaused:
            self._ispaused = False
            self.otherbutton.config(text='Stop Sign')
        else:
            self._ispaused = True
            self.otherbutton.config(text='Traffic Light')
            
    def desired(self):
        if self._ispaused:
            self._ispaused = False
            self.button2.config(text='Stop Sign')
        else:
            self._ispaused = True
            self.button2.config(text='Traffic Light')
            
    def desiredSign2(self):
        if self._ispaused:
            self._ispaused = False
            self.otherbutton2.config(text='Stop Sign')
        else:
            self._ispaused = True
            self.otherbutton2.config(text='Traffic Light')
            
            
    

    
Signs()