# 创建字典

# 使用花括号创建字典
scores = {'语文': 89, "数学": 100, "英语": 91}
print(scores)
# 空字典
empty_dict = {}
print(empty_dict)

# 使用元组作为可以
dict1 = {(20, 30): 'good', 30: 'bad'}
print(dict1)

# 使用dict()函数创建字典时，可以传入多个列表或元组参数作为key-value对，每个列表或元组将被当成一个key-value，因此这些列表和元组只能包含两个元素
vegetables = [('celery', 1.58), ('brocolo', 1.29), ('lettuce', 2.19)]
dict2 = dict(vegetables)
print(dict2)

cars = [['BMW', 8.5], ['BENS', 9], ['AUDI', 7]]
dict3 = dict(cars)
print(dict3)

# 空字典
dict4 = dict()
print(dict4)

# 可通过指定关键字参数创建字典，此的key不允许使用表达式
dict_5 = dict(spinach=1, cabbage=2)
print(dict_5)
