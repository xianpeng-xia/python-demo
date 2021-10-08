# 使用%进行格式化输出
price = 108
print("the book's price is %s" % price)
user = 'Charlie'
age = 8
print("%s is a %s year old boy" % (user, age))

# -：指定左对齐，+：表示数值总带上符号，0：表示不补充空格，而是补充0
num = 30
print("num is: %06d" % num)
print("num is: %+06d" % num)
print("num is: %-6d" % num)

# 精确度
value = 3.1234556789
print("value is: %8.3f" % value)  # 最小宽度为8，小数点保留3位
print("value is: %08.3f" % value)  # 最小宽度为8，小数点保留3位，左边补0
print("value is: %+08.3f" % value)  # 最小宽度为8，小数点保留3位，左边补0，始终带符号

name = "Charlie"
# 保留3个字符
print("the name is: %.3s" % name)
# 保留2个字符,最小宽度是10
print("the name is: %10.2s" % name)
