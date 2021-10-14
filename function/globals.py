# globals()test
name = "tom"


def test():
    # 函数中声明是全局变量，再对全局变量进行修改
    global name
    name = "Bob"
    print(name)


test()
print(name)

# 访问被遮蔽的全局变量
def test2():
    print(globals()['name'])
    name = 'Lisa'
    print(name)


test2()
print(name)
