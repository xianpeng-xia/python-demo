# 列表的其他常用方法

# --- count() 统计列表中某个元素出现的次数
a_list = [2, 30, 'a', [5, 30], 30]
print(a_list.count(30))
print(a_list.count([5, 30]))

# --- index() 判断某个元素在列表中出现的位置，可指定start，end参数
b_list = [2, 30, 'a', 'b', 'cde', 30]
print(b_list)
print(b_list.index(30))
# 从索引2开始，元素30出现的位置
print(b_list.index(30, 2))
# print(b_list.index(30, 2, 4)) # 找不到该元素报ValueError错误

# --- pop() 出栈
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
print(stack)

# 出栈
print(stack.pop())
print(stack)
# 出栈
print(stack.pop())
print(stack)
# --- reverse() 将列表元素反向存放
c_list = list(range(1, 8))
print(c_list)
c_list.reverse()
print(c_list)

# --- sort() 排序
d_list = [3, 4, -2, -30, 12, 9.2, 2.4, 83, 22, -1]
print(d_list)
d_list.sort()
print(d_list)

e_list = ['s', 'a', 'f', 'a', 'r', 'd']
print(e_list)
e_list.sort()
print(e_list)

# key参数用于为每个元素生成一个比较大小的键，reverse参数用于执行是否需要反转排序-默认从小到大
f_list = ['abc', 'eeedsgg', 'ssdf', 'aaerrssaas', 'ssss']
print(f_list)
f_list.sort(key=len)
print(f_list)
f_list.sort(key=len, reverse=True)
print(f_list)
