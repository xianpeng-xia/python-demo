# 重写__repr__()方法：
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 自我描述功能
    def __repr__(self):
        return "Item[name = " + self.name + ", price = " + str(self.price) + "]"


im = Item("鼠标", 100)
# 输出im所引用的对象
print(im)
