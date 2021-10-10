# 修改列表元素

a_list = ['a', 1, 2, 6, 7, 'b', 3]
print(a_list)

# 对第3个元素赋值
a_list[2] = 1
print(a_list)

# 对倒数第2个元素赋值
a_list[-2] = -1
print(a_list)

# slice语法
b_list = list(range(1, 5))
print(b_list)
# 将第2个到第4个(不包含)元素赋值为新列表的元素
b_list[1:3] = ['a', 'b']
print(b_list)
# 如果对列表中的空slice赋值，就变成了为列表插入元素
b_list[2:2] = ['x', 'y']
print(b_list)

# 将列表其中一段赋值为空列表，相当与从列表删除元素
b_list[2:5] = []
print(b_list)

# 对列表使用呢slice语法赋值时，不能使用单个值，如果使用字符串赋值，Python会自动把字符串当成序列处理
b_list[1:3] = 'Charlie'
print(b_list)

# 使用slice语法赋值时，如果指定了step参数，则要求所赋值的列表元素个数与所替换的列表元素个数相等
c_list = list(range(1, 10))
c_list[2:9:2] = ['a', 'b', 'c', 'd']
print(c_list)
