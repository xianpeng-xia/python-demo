# 加法

a_tuple = ('a', 20, -1.2)
b_tuple = (127, 'a', 'b', 3.333)

sum_tuple = a_tuple + b_tuple

print(sum_tuple)
print(a_tuple)
print(b_tuple)

#
print(a_tuple + (-20, -30))

a_list = [20, 20, 50, 100]
b_list = ['a', 'b', 'c']

sum_list = a_list + b_list
print(sum_list)
print(a_list + ['d'])
