# 局部函数

def get_math_func(type, nn):
    # 求平方
    def square(n):
        return n * n

    # 求立方
    def cube(n):
        return n * n * n

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    if type == 'square':
        return square(nn)
    elif type == 'cube':
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func("square", 4))
print(get_math_func("cube", 4))
print(get_math_func("factorial", 4))
