# 函数的多个返回值

# 可将多个值包装成列表返回，也可直接返回多个值

def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


list = [1, 2, 3, 4, 5, 6]
tp = sum_and_avg(list)
print(tp)
# 使用解包获取多个返回值
sum, avg = sum_and_avg(list)
print(sum)
print(avg)
