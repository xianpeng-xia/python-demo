# 逻辑运算符

# and
print(5 > 3 and 20.0 > 20)
# or
print(4 >= 5 or "c" > "a")
# not
print(not False)

# 组合逻辑运算

bookName = "Python"
price = 79
version = "正式版本"
if bookName.endswith("Python") and (price < 50 or version == "正式版本"):
    print("买")
else:
    print("不买")
