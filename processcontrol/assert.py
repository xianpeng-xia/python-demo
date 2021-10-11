# 断言

s_age = input("请输入年龄：")
age = int(s_age)
assert 20 < age < 80
# 条件为false，引发AssertionError错误
print("年龄在20-80之间")
