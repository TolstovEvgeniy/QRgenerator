from tkinter import *


class Buttons:
    def __init__(self, area, text_button, command):
        self.area = area
        self.text_button = text_button
        self.command = command
        self.button = Button(self.area, text=self.text_button, command=self.command)

    def button_draw(self):
        self.button.pack()
