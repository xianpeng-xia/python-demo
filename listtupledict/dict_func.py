# 字典的常用方法:clear(),get(),update(),items(),keys(),values(),pop(),popitem(),setdefault(),fromkeys(),使用字典格式化字符串

# clear() 清空字典中的所有key-value对
cars_dict = {'BMW': 8.5, 'BENS': 9, 'AUDI': 7}
print(cars_dict)
cars_dict.clear()
print(cars_dict)

# get() 根据key获取元素,获取不到会返回Noe
cars_dict = {'BMW': 8.5, 'BENS': 9, 'AUDI': 7}
print(cars_dict.get('BMW'))
print(cars_dict.get('AUTO'))

# update(): 如果被更新的字典中已包含则覆盖，否则添加进去
cars_dict.update({'AUDI': 9, 'AUTO': 6})
print(cars_dict)

# items() 获取字典中的所有key-value对，返回一个dict-items对象
ims = cars_dict.items();
print(type(ims))
print(ims)
# 将dict_items转成列表
print(list(ims))
print(list(ims)[1])

# keys() 获取字典中的所有key，返回一个dict-keys对象
keys = cars_dict.keys()
print(type(keys))
print(keys)
print(list(keys))
print(list(keys)[1])

# values() 获取字典中的所有value，返回一个dict-values对象
values = cars_dict.values()
print(type(values))
print(values)
print(list(values))
print(list(values)[1])

# pop() 获取指定key对应的value，并删除这个key-value对
print(cars_dict.pop('AUTO'))
print(cars_dict)

# popitem() 随机弹出字典中对一个key-value对
print(cars_dict.popitem())
print(cars_dict)

# setdefault() 如果不存在则设置一个默认的value，如果存在则不修改dict内容
print(cars_dict.setdefault('PORSCHE', 9.3))
print(cars_dict)
print(cars_dict.setdefault('BMW', 9.3))
print(cars_dict)

# fromkeys() 给指定的多个key创建字典，默认值是None，可传入默认值

a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)
b_dict = dict.fromkeys((1, 2))
print(b_dict)

c_dict = dict.fromkeys((1, 2), 'good')
print(c_dict)

# 使用字典格式化字符串
temp = '书名是：%(name)s，价格是：%(price)010.2f，出版社是：%(publish)s'
book = {'name': '百年孤独', 'price': 150.02, 'publish': '人民出版社'}
print(temp % book)
