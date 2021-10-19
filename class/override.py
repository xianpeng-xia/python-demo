# 重写父类方法

class Bird:
    def fly(self):
        print("fly...")


class Ostrich(Bird):
    def fly(self):
        print("i can't fly...")


ostrich = Ostrich()
ostrich.fly()
