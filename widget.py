from field import *
from PIL import Image, ImageTk


class TopFrame:
    def __init__(self, root):
        self.root = root
        self.top_frame = LabelFrame(self.root, text='Параметры QR')
        self.field_free = Field(self.top_frame, "Свободный текст")
        self.field_free.entry.config(state=NORMAL)
        self.field_free.variable_int.set(1)
        self.field_company = Field(self.top_frame, "Компания")
        self.field_cabinet = Field(self.top_frame, "Кабинет")
        self.field_type = Field(self.top_frame, "Тип техники")
        self.field_date = Field(self.top_frame, "Дата")

    def draw_top_frame(self):
        self.top_frame.pack(anchor=N, fill=BOTH, padx=5, pady=5)
        self.field_free.draw_field()
        self.field_company.draw_field()
        self.field_company.draw_field()
        self.field_cabinet.draw_field()
        self.field_type.draw_field()
        self.field_date.draw_field()

    def get_values_date(self):
        qrsingl.value_dict.clear()
        qrsingl.value_string = ''
        self.field_free.get_value()
        self.field_company.get_value()
        self.field_cabinet.get_value()
        self.field_type.get_value()
        self.field_date.get_value()


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

    def output_value(self):
        self.label_value_qr.config(text=qrsingl.value_string)

    def lable_image_value(self):
        image = qrsingl.image
        image_resize = image.resize((300, 300))
        image_tk = ImageTk.PhotoImage(image_resize)
        self.label_image_qr.configure(image=image_tk)
        self.label_image_qr.image = image_tk