# while循环

# 循环的初始条件
count_i = 0
while count_i < 10:
    # 循环体
    print("count = ", count_i)
    # 迭代语句
    count_i += 1
print("循环结束")

# 循环遍历tuple
a_tuple = ('a', 'b', 'c')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

# 循环遍历list
src_list = [12, 4, 2, 6, 7, 8, 9, 11, 22, 21]
# 整除3的
a_list = []
# 余1
b_list = []
# 余2
c_list = []

while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3的：", a_list)
print("整除3余1的：", b_list)
print("整除3余2的：", c_list)
