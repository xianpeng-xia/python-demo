# 使用函数作为返回值

def get_math_func(type):
    def square(n):
        return n * n

    def cube(n):
        return n * n * n

    if type == 'square':
        return square
    elif type == "cube":
        return cube
    else:
        return square


math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("cube")
print(math_func(5))
