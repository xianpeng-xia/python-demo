# 使用property函数定义属性

# ---对Rectangle对象对size属性的读写删除操作，被委托给getsize(),setsize(),delsize()方法来实现
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setsize(self, size):
        self.width, self.height = size

    def getsize(self):
        return self.width, self.height

    def delsize(self):
        self.width, self.height = 0, 0

    # 使用property函数定义属性
    size = property(getsize, setsize, delsize, "描述矩形大小的属性")


print(Rectangle.size.__doc__)
help(Rectangle.size)

rect = Rectangle(3, 4)
# 查询
print(rect.size)
# 修改
rect.size = 9, 7
print(rect.width)
print(rect.height)
# 删除
del rect.size
print(rect.width)
print(rect.height)


# --- property函数可传少量参数
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + "," + self.last

    def setfullname(self, fullname):
        f_l = fullname.rsplit(',')
        self.first = f_l[0]
        self.last = f_l[1]

    fullname = property(getfullname, setfullname)


u = User("悟空", "孙")
print(u.fullname)
u.fullname = "八戒,朱"
print(u.first)
print(u.last)


# del u.fullname

# --- 可以使用@property修饰方法，使之成为属性

class Cell:
    # 修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state

    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
c.state = 'Alive'

print(c.state)
print(c.is_dead)
