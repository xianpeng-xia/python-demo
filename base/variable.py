# 变量


# 定义数值类型a
a = 5
print(a)
# 重新将字符串赋值给a
a = "Hello，Charlie"
print(a)
print(type(a))

# 使用print函数输出变量

'''
print函数语法格式

print(value,...sep=' ',end='\n',file=sys.stdout,f;ush=False)
'''

user_name = 'Charlie'
user_age = 8
# 使用print函数输出变量
print("读者名:", user_name, "读者年龄:", user_age)
# 使用print函数指定分隔符输出变量
print("读者名:", user_name, "读者年龄:", user_age, sep='|')

# 使用print函数指定end参数(默认换行)
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")

# 使用print函数指定file参数(默认换行)
f = open("poem.text", "w")  # 打开文件以便于写入
print('a', file=f)
print("b", file=f)
f.close()

# print()函数的flush参数用于控制输出缓存
