s1 = "价格:"
p = 99.9
# 使用str()函数将数值转化为字符串
print(s1 + str(p))
# 使用repr()函数将数值转化为字符串
print(s1 + repr(p))

# str()函数与repr()函数区别:repr()以python的表达式形式表示值

st = 'I will play my fife'
print(str(st))
print(repr(st))
