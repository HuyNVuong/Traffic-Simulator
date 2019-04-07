from CommandPallete import CommandPallete
from tkinter import Tk
from PyQt5 import QtCore, QtWidgets

def test_start_button(qtbot):
    root = Tk()
    command = CommandPallete(master=root)
    qtbot.addWidget(command)
    qtbot.mouseClick(command.start_button, QtCore.Qt.LeftButton)