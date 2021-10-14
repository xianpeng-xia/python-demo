# 关键字参数

def girth(width, height):
    print("width = ", width)
    print("height = ", height)
    return 2 * (width + height)


# 根据位置传入参数值
print(girth(3, 4))
# 根据关键字参数传入参数值
print(girth(height=4, width=3))
# 部分使用关键字参数，部分使用位置参数，关键字参数必须位于位置参数之后
print(girth(3, height=4))
