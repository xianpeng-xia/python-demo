# locals()测试
def locals_test():
    age = 20
    print(age)

    print(locals())

    print(locals()['age'])
    # 修改变量字典的值，不生效
    locals()['age'] = 20

    print(age)
    # 全局范围内对x赋值生效
    globals()['x'] = 99
    print(globals()['x'])


locals_test()
x = 5
y = 6
print(x, y)

print(locals())
print(globals())

print(globals()['x'])

globals()['x'] = 0
print(x)
# 全局范围内对x赋值生效
locals()['x'] = 1
print(x)
