from tkinter import *


class Widget:
    def __init__(self, root):
        self.root = root
        self.top_frame = LabelFrame(self.root, text='Параметры QR')
        self.bottom_frame = LabelFrame(self.root, text='Просмотр QR')

        self.frame_1 = Frame(self.top_frame, padx=10, pady=10)
        self.frame_2 = Frame(self.top_frame)
        self.frame_3 = Frame(self.top_frame)
        self.frame_4 = Frame(self.top_frame)
        self.frame_5 = Frame(self.top_frame)
        self.frame_6 = Frame(self.top_frame)

        self.var_free_int = IntVar()
        self.var_organization_int = IntVar()
        self.var_index_int = IntVar()
        self.var_type_int = IntVar()
        self.var_room_int = IntVar()
        self.var_date_int = IntVar()

        # b1 = Button(self.top_frame, text='asd', command=lambda:print(self.int_var_free.get())).pack()

        self.free_label = Label(self.frame_1, text='Свободный текст:', font='System 11 bold', width=16, anchor=E)
        self.organization_label = Label(self.frame_2, text='Организация:', font='System 11 bold', width=16, anchor=E)
        self.index_label = Label(self.frame_3, text='Индекс:', font='System 11 bold', width=16, anchor=E)
        self.type_label = Label(self.frame_4, text='Типи техники:', font='System 11 bold', width=16, anchor=E)
        self.room_label = Label(self.frame_5, text='Кабинет:', font='System 11 bold', width=16, anchor=E)
        self.date_label = Label(self.frame_6, text='Дата:', font='System 11 bold', width=16, anchor=E)

        self.free_entry = Entry(self.frame_1, width=30, state=NORMAL)
        self.organization_entry = Entry(self.frame_2, width=30, state=DISABLED)
        self.index_entry = Entry(self.frame_3, width=30, state=DISABLED)
        self.type_entry = Entry(self.frame_4, width=30, state=DISABLED)
        self.room_entry = Entry(self.frame_5, width=30, state=DISABLED)
        self.date_entry = Entry(self.frame_6, width=30, state=DISABLED)

        self.free_check = Checkbutton(self.frame_1, anchor=E, variable=self.var_free_int, command=self.entry_enable)
        self.organization_check = Checkbutton(self.frame_2, anchor=E, variable=self.var_organization_int, command=self.entry_enable)
        self.index_check = Checkbutton(self.frame_3, anchor=E, variable=self.var_index_int, command=self.entry_enable)
        self.type_check = Checkbutton(self.frame_4, anchor=E, variable=self.var_type_int, command=self.entry_enable)
        self.room_check = Checkbutton(self.frame_5, anchor=E, variable=self.var_room_int, command=self.entry_enable)
        self.date_check = Checkbutton(self.frame_6, anchor=E, variable=self.var_date_int, command=self.entry_enable)

        self.free_check.toggle()

        self.label_value_qr = Label(self.bottom_frame, text='"Расшифровка QR"', relief=SOLID)
        self.label_image_qr = Label(self.bottom_frame, text='Картинка QR', relief=RIDGE, padx=100, pady=127)

    def draw_widget(self):
        self.top_frame.pack(anchor=N, fill=BOTH, padx=5, pady=5)

        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()

        self.free_label.pack(side=LEFT)
        self.organization_label.pack(side=LEFT)
        self.index_label.pack(side=LEFT)
        self.type_label.pack(side=LEFT)
        self.room_label.pack(side=LEFT)
        self.date_label.pack(side=LEFT)

        self.free_entry.pack(side=LEFT)
        self.organization_entry.pack(side=LEFT)
        self.index_entry.pack(side=LEFT)
        self.type_entry.pack(side=LEFT)
        self.room_entry.pack(side=LEFT)
        self.date_entry.pack(side=LEFT)

        self.free_check.pack(side=LEFT)
        self.organization_check.pack(side=LEFT)
        self.index_check.pack(side=LEFT)
        self.type_check.pack(side=LEFT)
        self.room_check.pack(side=LEFT)
        self.date_check.pack(side=LEFT)

        self.bottom_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.label_value_qr.pack(fill=X, padx=5, pady=5)
        self.label_image_qr.pack(padx=5, pady=5)

    def entry_enable(self):
        list_entry_var = [
            self.var_free_int,
            self.var_organization_int,
            self.var_index_int,
            self.var_type_int,
            self.var_room_int,
            self.var_date_int
        ]

        list_entry = [
            self.free_entry,
            self.organization_entry,
            self.index_entry,
            self.type_entry,
            self.room_entry,
            self.date_entry
        ]

        len_elem = len(list_entry_var)

        for elem in range(len_elem):
            if list_entry_var[elem].get() == 1:
                list_entry[elem].config(state=NORMAL)
            else:
                list_entry[elem].delete(0, END)
                list_entry[elem].config(state=DISABLED)
