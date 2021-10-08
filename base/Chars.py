s = 'the book is very good'
# 获取s中索引为2的字符
print(s[2])

# 获取s中从右边开始，索引为4的字符
print(s[-4])

# 获取s中索引为3到索引5(不包含)的字符
print(s[3:5])

# 获取s中索引为3到索引为倒数第5个字符的字符
print(s[3:-5])

# 获取s中倒数第6个字符到倒数第3个字符的字符
print(s[-6:-3])

# 从索引5到结束
print(s[5:])

# 从开始到索引5
print(s[:5])

# 使用in判断是否包含某个子串
print("very" in s)

# 获取字符串长度
print(len(s))

# 最大，最小字符
print(max(s) + ":" + min(s))
