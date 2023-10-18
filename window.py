from tkinter import *

#from PIL import Image, ImageTk
#from tkinter import filedialog
from menu import MenuBar
from widget import Widget
from tkinter import messagebox


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("QR Генератор")
        # self.root.iconphoto(True, PhotoImage(file='resources/iconQR.png'))
        self.root.minsize(400, 500)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.menu_bar = MenuBar(self.root)
        self.widget = Widget(self.root)

    def run(self):
        self.menu_bar.draw_menu()
        self.widget.draw_widget()
        self.root.mainloop()

    #def open_new_image(self):
        #image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpeg;*.jpg;*.png'),))
        #image = Image.open(image_path)

        #image_resize = image.resize((300, 300))

        #image_tk = ImageTk.PhotoImage(image_resize)
        #self.label_image_qr.configure(image=image_tk)
        #self.label_image_qr.image = image_tk

    def exit(self):
        if messagebox.askyesno('Выход', 'Вы действительно хотите выйти из приложения?'):
            self.root.destroy()


if __name__ == '__main__':
    window = Window()
    window.run()
