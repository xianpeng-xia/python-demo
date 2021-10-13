# 常用函数

# --- zip()压缩函数：
# 使用zip函数压缩N个列表，返回的可迭代对象的元素就是长度为N的元组，
# 如果列表长度不想等，以最小的为准

a = ['a', 'b', 'c']
b = [1, 2, 3]
print([x for x in zip(a, b)])
c = [0.1, 0.2]
print([x for x in zip(a, c)])
print([x for x in zip(a, b, c)])

# 使用zip()函数实现并行遍历
books = ['百年孤独', '老人与海', '红楼梦']
prices = [100, 99, 98]
for book, price in zip(books, prices):
    print('book: %s , price: %d' % (book, price))

# --- reversed()反向排序,不改变原始对象
a = range(10)
for x in reversed(a):
    print("x = ", x)
print(a)

#
for x in sorted(a):
    print("x = ", x)
