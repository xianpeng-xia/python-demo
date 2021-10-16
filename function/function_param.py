# 使用函数作为函数参数
def map(data, fn):
    result = []
    for e in data:
        result.append(fn(e))
    return result


# 计算平方
def square(n):
    return n * n


# 计算立方
def cube(n):
    return n * n * n


data = [1, 2, 3, 4]

print(map(data, square))
print(map(data, cube))
# map的类型是function
print(type(map))
