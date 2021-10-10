# 元组的创建

a_list = ['a', 1, 2]
a_tuple = tuple(a_list)
print(a_tuple)

# 将区间转成元组
a_range = range(1, 5)
print(a_range)
b_tuple = tuple(a_range)

# 创建区间指定步长
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)
