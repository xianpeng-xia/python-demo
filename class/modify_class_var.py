# 类变量与实例变量
class Inventory:
    item = "鼠标"
    quantity = 2000

    def change(self, item, quantity):
        self.item = item
        self.quantity = quantity


# 如果程序通过对象对类变量赋值，是定义新的实例变量
iv = Inventory()
iv.change("键盘", 500)
print(iv.item)
print(iv.quantity)
print(Inventory.item)
print(Inventory.quantity)

# 修改了类变量的值，实例变量的值不受影响
Inventory.item = "类变量item"
Inventory.quantity = "类变量quantity"
print(iv.item)
print(iv.quantity)

# 修改了实例变量的值，类变量的值不受影响
iv.item = "实例变量item"
iv.quantity = "实例变量quantity"
print(Inventory.item)
print(Inventory.quantity)
