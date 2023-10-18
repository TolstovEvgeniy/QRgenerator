from tkinter import *
from tkinter import messagebox


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.info_menu = Menu(self.menu_bar, tearoff=0)

    def draw_menu(self):
        self.file_menu.add_command(label='Открыть QR-код')
        self.file_menu.add_command(label='Сохранить')
        self.file_menu.add_command(label='Сохранить как')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Выход')

        self.info_menu.add_command(label='О приложении', command=self.show_info)

        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)
        self.menu_bar.add_cascade(label='Справка', menu=self.info_menu)
        self.root.configure(menu=self.menu_bar)

    @staticmethod
    def show_info():
        messagebox.showinfo('Информация', 'Версия приложения: 0.0.13')
