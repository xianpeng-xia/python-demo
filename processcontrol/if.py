# if分支结构
s_age = 45  # input("请输入你的年龄：")
age = int(s_age)

# ---
if age > 20:
    # 锁进(4个空格)，位于同一个代码块的所有语句必须保持相同的锁进,':'精确表示代码块的开始点
    print("年龄超过20!")
    print("20岁以上的人应该学会承担责任...")

# --- if条件的类型
# 当下面的值作为bool表达式时，会被解释器当成False处理：False,None,0,"",'',(),{},[]
s = ""
if s:
    print("s不是空字符串")
else:
    print("s是空字符串")

empty_list = []
if empty_list:
    print('list不是空列表')
else:
    print('list是空列表')

empty_dict = {}
if empty_dict:
    print("dict不是空字典")
else:
    print("dict是空字典")

# 使用if else分支语句时，一定要先处理包含范围更小的情形
age = 45
if age > 60:
    print("老年人")
elif age > 40:
    print("中年人")
else:
    print("青年人")

# pass语句
num = 4
if num > 5:
    print("大于5")
elif num < 5:
    pass
else:
    print("等于5")
