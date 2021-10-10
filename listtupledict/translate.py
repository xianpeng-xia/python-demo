# 同时对元组使用加法，乘法

# ('th',)表示只有一个元素的元组，('th')与'th'相同，并不表示元组
order_endnings = ('st', 'nd', 'rd') + ('th',) * 17 + ('st', 'nd', 'rd') + ('th',) * 7 + ('st',)  # 每月第x天后缀
print(order_endnings)
day = input("输入日期【1-31】：")
# 将字符串转为int
day_int = int(day)
print(day + order_endnings[day_int - 1])
