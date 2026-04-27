#8-misol
class Ota:
    def __init__(self, ism):
        self.ism = ism

    def gapir(self):
        print("Gapirdi")


class Ogil(Ota):
    def gapir(self):
        print("O‘g‘il gapirdi")


o1 = Ota("Hasan")
o2 = Ogil("Husan")

o1.gapir()
o2.gapir()
