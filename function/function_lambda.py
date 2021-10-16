#  使用lambda表达式替代局部函数

def get_math_func(type):
    if type == 'square':
        return lambda n: n * n
    elif type == "cube":
        return lambda n: n * n * n
    else:
        return lambda n: n


math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("cube")
print(math_func(5))
