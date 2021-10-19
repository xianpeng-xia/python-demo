# 如果希望创建某一批类都具有某些特征。可通过metaclass实现
# metaclass类的__new__()方法的作用是：当程序使用class重新定义类，如果指定了metaclass，那么metaclass的__new__方法就会被自动执行
class ItemMetaClass(type):
    # cls: 被动态修改的类
    # name: 被动态修改的类名
    # bases: 被动态修改的类的所有父类
    # attrs: 被动态修改的类的所有属性，方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 为该类动态添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)


class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


b = Book("百年孤独", 100)
b.discount = 0.8
print(b.cal_price())

cp = CellPhone(100)
cp.discount = 1
print(cp.cal_price())
