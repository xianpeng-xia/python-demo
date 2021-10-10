# 删除列表元素

a_list = ['a', 'b', 1, 4, 9, 3, 2, 5, 0, 1.1]
# 删除第三个元素
del a_list[2]
print(a_list)

# 删除第2到第4个(不包含)元素
del a_list[1:3]
print(a_list)

# 删除第3个到倒数第2个(不包含)，间隔为2
del a_list[2:-2:2]
print(a_list)

# 删除
del a_list[2:4]
print(a_list)

# 删除变量
name = 'tom'
del name
# print(name) # 报NameError错

# 根据元素本身删除元素
a_list.remove(9)
print(a_list)

a_list.remove(9)  # 报ValueError错
print(a_list)
