class Person:
    # 定义一个类变量
    hair = 'black'

    # 构造函数
    def __init__(self, name='Charlie', age=9):
        self.name = name
        self.age = age

    # 方法
    def say(self, content):
        print(content)


p = Person()
# 输出p的实例变量
print(p.name, p.age)
# 修改实例变量
p.name = 'Tom'
print(p.name, p.age)
# 调用方法
p.say("hello")

# --- 对象的动态性
p.skills = ['programming', 'swimming']
print(p.skills)

# 删除name属性
del p.name


# 报AttributeError错
# print(p.name)

# 定义一个方法
def info(self):
    print("---info 函数---", self)


# 动态增加方法，但是self必须当参数传递，即使参数名为self也无用
p.foo = info
p.foo(p)

#  动态增加方法:使用lambda表达式为p对象的bar赋值
p.bar = lambda self: print("---lambda表达式---", self)
p.bar(p)


# 动态增加方法：希望能自动绑定第一个参数，使用MethodType进行包装
def intro_func(self, content):
    print("i'm a person,content : ", content)


from types import MethodType

p.intro_func = MethodType(intro_func, p)
p.intro_func("live in beijing")
