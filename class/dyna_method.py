# 为类添加方法
class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print('%s walk ... ' % (self.name))


d1 = Cat("Garfield")
d2 = Cat("Kitty")
# 动态增加方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func
d1.walk()
d2.walk()
