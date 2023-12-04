from menu import MenuBar
from widget import *
from tkinter import messagebox


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("QR Генератор")
        # self.root.iconphoto(True, PhotoImage(file='resources/iconQR.png'))
        self.root.minsize(400, 500)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.menu_bar = MenuBar(self.root)
        self.top_frame = TopFrame(self.root)
        self.button = Button(self.root, text='Сгенерировать QR', command=self.button_generator)
        self.bottom_frame = BottomFrame(self.root)

    def button_generator(self):
        self.top_frame.get_values_date()
        qrsingl.value_to_string()
        self.bottom_frame.output_value()
        qrsingl.qr_make()
        self.bottom_frame.lable_image_value()

    def run(self):
        self.menu_bar.draw_menu()
        self.top_frame.draw_top_frame()
        self.button.pack()
        self.bottom_frame.draw_bottom_frame()
        self.root.mainloop()

    def exit(self):
        if messagebox.askyesno('Выход', 'Вы действительно хотите выйти из приложения?'):
            self.root.destroy()


if __name__ == '__main__':
    window = Window()
    window.run()
