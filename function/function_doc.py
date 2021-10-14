# 为函数提供文档,函数声明之后，函数体之前的字符串

def i_max(x, y):
    '''
    获取两个数中的较大数
    :param x: 数字x
    :param y: 数字y
    :return: x，y中较大者
    '''
    return x if x > y else y;


# 可使用help()查看函数的说明文档
help(i_max)
# 可通过__doc__查看函数的说明文档
print(i_max.__doc__)
