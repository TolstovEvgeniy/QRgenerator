from tkinter import *


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


class TopFrame:
    def __init__(self, root):
        self.root = root
        self.top_frame = LabelFrame(self.root, text='Параметры QR')
        self.field_free = Field(self.top_frame, "Свободный текст:")
        self.field_free.entry.config(state=NORMAL)
        self.field_free.variable_int.set(1)
        self.field_company = Field(self.top_frame, "Компания")
        self.field_cabinet = Field(self.top_frame, "Кабинет")
        self.field_type = Field(self.top_frame, "Тип техники")
        self.field_data = Field(self.top_frame, "Дата")

    def draw_top_frame(self):
        self.top_frame.pack(anchor=N, fill=BOTH, padx=5, pady=5)
        self.field_free.draw_field()
        self.field_company.draw_field()
        self.field_company.draw_field()
        self.field_cabinet.draw_field()
        self.field_type.draw_field()
        self.field_data.draw_field()


class BottomFrame:
    def __init__(self, root):
        self.root = root
        self.bottom_frame = LabelFrame(self.root, text='Просмотр QR')
        self.label_value_qr = Label(self.bottom_frame, text='"Расшифровка QR"', relief=SOLID)
        self.label_image_qr = Label(self.bottom_frame, text='Картинка QR', relief=RIDGE, padx=100, pady=127)

    def draw_bottom_frame(self):
        self.bottom_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.label_value_qr.pack(fill=X, padx=5, pady=5)
        self.label_image_qr.pack(padx=5, pady=5)
