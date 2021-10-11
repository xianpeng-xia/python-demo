# for-in循环

# --- 计算阶乘
max_num = 7
result = 1
for num in range(1, max_num + 1):
    result *= num
print(result)

# --- 遍历元组/列表
a_tuple = ('a', 'b', 'c')
for ele in a_tuple:
    print('元素：', ele)

# 遍历列表，对数值进行求和以及算平均值
a_list = ['a', 1, 2, 3, 1.5, 7.2]
total = 0
count = 0
for ele in a_list:
    # isinstance()判断是否是指定类型
    if isinstance(ele, int) or isinstance(ele, float):
        total += ele
        count += 1
print("total  = ", total)
print("count = ", total / count)

# --- 遍历字典
score_dict = {'语文': 90, '数学': 100}
for key, value in score_dict.items():
    print("key: ", key)
    print("value: ", value)

for key in score_dict.keys():
    print("key: ", key)

for value in score_dict.values():
    print("value: ", value)

# --- 统计各元素出现次数
src_list = [12, 2, 12, 1, 2, 'a', 'b', 'a', 'd']
statistics = {}
for ele in src_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1

for ele, count in statistics.items():
    print("%s出现的次数为:%d" % (ele, count))
