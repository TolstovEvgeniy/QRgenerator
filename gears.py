import qrcode


class Qr:
    def __init__(self):
        self.value = {}
        self.image = None
        self.name = None

    def qr_make(self):
        self.image = qrcode.make(self.value)

    def save_ass(self):
        self.image.save(f'{self.name}')
