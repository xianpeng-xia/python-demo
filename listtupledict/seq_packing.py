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
