# 序列封包和序列解包

# 序列封包
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])

# 序列解包
a_tuple = tuple(range(1, 10, 2))
a, b, c, d, e = a_tuple
print(a, b, c, d, e)

a_list = ['a', 'b']
a_str, b_str = a_list
print(a_str, b_str)

# 同时使用序列封包和序列解包机制
x, y, z = 10, 20, 30
print(x, y, z)

x, y, z = y, z, x  # 实现交换变量的值
print(x, y, z)

# 可以只解出部分变量，剩余的依然使用列表变量保存(*变量)
first, second, *rest = range(10)
print(first)
print(second)
print(rest)

*begin, last = range(10)
print(begin)
print(last)

first, *middle, last = range(10)
print(first)
print(middle)
print(last)
