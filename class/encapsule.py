# 封装

class User:
    def __hide(self):
        print("hide func")

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('名字长度必须在3-8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('年龄必须在18-70之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


u = User()
# 会ValueError报错
# u.name = 'fk'
# u.age = 1
u.name = 'fkfk'
u.age = 20
print(u.name)
print(u.age)
# 报AttributeError错
# u.__hide()

# 可以如下方式调用(不推荐)
u._User__hide()
u._User__name = 'fk'
print(u.name)

