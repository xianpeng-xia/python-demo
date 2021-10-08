# 比较运算符
import time

# >
print("5 > 4:", 5 > 4)

# >=
print("3 ** 4 > 90:", 3 ** 4 > 90)

# ==
print("5 == 5.0:", 5 == 5.0)

# 1 == True
print("1 == True:", 1 == True)

# 0 == False
print("0 == False:", 0 == False)

# is 判断两个变量所引用的对象是否相同
time1 = time.gmtime()
time2 = time.gmtime()
print(time1 == time2)
# is判断是根据id()函数计算出的内存地址判断是否是同一个对象
print(id(time1))
print(id(time2))
print(time1 is time2)
print(time1 is not time2)
