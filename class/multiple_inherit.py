# 多继承，相同方法名，优先找前面定义的父类方法

class Item:
    def info(self):
        print("Item中的方法", '这是一个商品')


class Product:
    def info(self):
        print("Product中的方法", '这是一个工业产品')


class Mouse(Item, Product):
    pass


m = Mouse()
# 优先找前面定义的父类方法
m.info()
