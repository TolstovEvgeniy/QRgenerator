from tkinter import *
from gears import *


class Field:
    def __init__(self, area, text_label):
        self.area = area
        self.text_label = text_label
        self.variable_int = IntVar()
        self.frame = Frame(self.area)
        self.label = Label(self.frame, text=self.text_label, font='System 11 bold', width=16, anchor=E)
        self.entry = Entry(self.frame, width=30, state=DISABLED)
        self.check_button = Checkbutton(self.frame, anchor=E, variable=self.variable_int, command=self.check_entry)

    def draw_field(self):
        self.frame.pack()
        self.label.pack(side=LEFT)
        self.entry.pack(side=LEFT)
        self.check_button.pack(side=LEFT)

    def check_entry(self):
        if self.variable_int.get() == 1:
            self.entry.config(state=NORMAL)
        else:
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)

    def get_value(self):
        if self.variable_int.get() == 1:
            qrsingl.value_dict[self.text_label] = self.entry.get()
