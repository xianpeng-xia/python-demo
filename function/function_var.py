# 使用函数变量

def area(x, y):
    return x * y


# my_func可当作area使用
my_func = area
print(my_func(3, 4))
