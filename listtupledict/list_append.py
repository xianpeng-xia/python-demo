# 增加列表元素

a_list = ['a', 1, 3, 1.6]
print(a_list)
# 追加一个元素
a_list.append("d")
print(a_list)

# 追加元组，元组被当成元素
a_tuple = (3.14, 6)
a_list.append(a_tuple)
print(a_list)

# 追加列表，列表被当成元素
b_list = [1, 'f', 's']
a_list.append(b_list)
print(a_list)

# 追加元组/列表中的所有元素
a_list.extend(a_tuple)
a_list.extend(b_list)
print(a_list)

# 追加区间中的所有元素
a_list.extend(range(97, 100))
print(a_list)

# 在列表中间增加元素
c_list = list(range(1, 6))
c_list.insert(3, 'c')
print(c_list)
# 插入元组，元组被当成一个元素
c_list.insert(3, tuple('crazy'))
print(c_list)
