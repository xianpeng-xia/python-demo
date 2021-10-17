# self在构造方法中，代表构造方法正在初始化的对象
class InConstructor:
    def __init__(self):
        foo = 0
        self.foo = 6


print(InConstructor().foo)
