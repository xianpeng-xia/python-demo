# 程序使用class定义的所有类都是type类的实例

def fn(self):
    print("fu func")


# 使用type()定义类
Dog = type("Dog", (object,), dict(walk=fn, age=6))
d = Dog()
print(type(d))  # <class '__main__.Dog'>
print(type(Dog))  # <class 'type'>
d.walk()
print(d.age)
