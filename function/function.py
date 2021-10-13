# 函数

# 求最大值
def i_max(x, y):
    return x if x > y else y


def say_hi(name):
    print('say hi...')
    return 'hi,' + name


a = 1
b = 2
result = i_max(a, b)
print(result)

print(say_hi('Bob'))
