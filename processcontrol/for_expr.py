# for表达式
# 在for关键字前定义一个表达式，该表达式通常会包含循环计数器
# for表达式没有循环体，不需要冒号

# --- 方括号的for表达式，返回的是列表
# 求每个元素的平方
a_range = range(1, 10)
a_list = [x * x for x in a_range]
print(a_list)

#  for表达式后面跟if条件
b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)

# --- 圆括号的for表达式，返回的是迭代器
c_generator = (x * x for x in a_range if x % 2 == 0)
print(type(c_generator))
for i in c_generator:
    print(i, end='\t')
print()

# --- for表达式多个循环
d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)

# 多个循环的for表达式，指定if条件
src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
e_list = [(x, y) for x in src_a for y in src_b if x % y == 0]
print(e_list)
