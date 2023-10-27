import qrcode


class Qr:
    def __init__(self):
        self.value_dict = dict()
        self.value_string = str()
        self.image = None
        self.name = None

    def value_to_string(self):
        strings = []
        for key, item in self.value_dict.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        self.value_string = ", ".join(strings)

    def qr_make(self):
        self.image = qrcode.make(self.value_string)

    def save_ass(self):
        self.image.save(f'{self.name}')

qrsingl = Qr()
