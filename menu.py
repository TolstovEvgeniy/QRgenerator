from tkinter import *
from tkinter import messagebox


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.menu_bar = Menu(self.root)

    def draw_menu(self):
        self.menu_bar.add_command(label='Сгенерировать QR')
        self.menu_bar.add_command(label='Сохранить как')
        self.menu_bar.add_command(label='Справка', command=self.show_info)
        self.root.configure(menu=self.menu_bar)

    @staticmethod
    def show_info():
        messagebox.showinfo('Информация', 'Версия приложения: 0.23.2')
