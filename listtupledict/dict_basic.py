# 字典的基本用法

scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])

# 对不存在的key赋值=添加key-value对
scores['数学'] = 100
print(scores)

# 删除字典中对key-value对
del scores['数学']
print(scores)

# 对已经存在对key-value赋值，会覆盖原有的value
scores['语文'] = 90
print(scores)

# 判断字典中是否包含指定key
print('语文' in scores)
print('数学' not in scores)
