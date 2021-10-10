# --- 创建列表

# tuple转化成列表
a_tuple = ('a', 1, 2, 1.2)
a_list = list(a_tuple)
print(a_list)

# 使用range()函数创建区间对象
a_range = range(1, 5)
print(a_range)
b_list = list(a_range)
print(b_list)

c_list = list(range(4, 20, 3))
print(c_list)
