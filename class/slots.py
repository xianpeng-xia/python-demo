# __slots__: 列出该类的实例允许动态添加的所有属性名和方法名
from types import MethodType


class Dog:
    # 列出该类的实例允许动态添加的所有属性名和方法名
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    def test(self):
        print("test func")


d = Dog("Snoopy")
d.walk = MethodType(lambda self: print("%s walk..." % (d.name)), d)
d.age = 5
d.walk()
#  报AttributeError错
# d.foo = 5

# __slots__属性不限制通过类动态添加属性和方法
Dog.bar = lambda self: print('bar')
d.bar()


# __slots__属性值对当前类的实例有效，对子类无效
class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    pass


gd = GunDog("Puppy")
gd.speed = 99
print(gd.speed)
