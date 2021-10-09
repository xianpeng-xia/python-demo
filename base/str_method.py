# 大小写转换
s = "our domain is c.org"
print(s.title())  # title() 将每个单词首字母改成大写
print(s.upper())  # upper() 将整个字符串改成大写
print(s.lower())  # lower() 将整个字符串改成小写

# 删除空白
s1 = ' this is a puppy '
print(s1)
print(s1.strip())  # strip()删除字符串前后的空白
print(s1.lstrip())  # lstrip()删除字符串前面的空白
print(s1.rstrip())  # rstrip()删除字符串后面的空白

# 查找，替换

s2 = 'tom is a good boy'
print(s2.startswith('tom'))  # startswith()判断是否以'tom'开头
print(s2.endswith('boy'))  # endswith()判断是否以'boy'结尾
print(s2.find('is'))  # find()查找'is'出现的位置，如果没有，返回-1
print(s2.index('is'))  # index()查找'is'出现的位置，如果没有，引发ValueError异常
print(s2.find('is', 9))  # find()从索引9开始查找'is'出现的位置，如果没有，返回-1

# 替换
print(s2.replace("a", 'b'))  # replace()将所有'a'替换为'b'
print(s2.replace("a", 'b', 1))  # replace()将第一个'a'替换为'b'

# 定义翻译表：
table = {97: 945, 98: 946, 99: 947}
print(s2.translate(table))  # translate()将所有'x'映射为对应'y'

# maketrans()定义翻译表
table = str.maketrans('abc', '123')
print(s2.translate(table))

# 分割，连接方法
s3 = 'this. is a good site'
print(s.split())  # split()将字符串指定分隔符分割成多个短语
print(s.split(None, 2))  # split()使用空白将字符串指定分隔符分割成多个短语，最多只分割前两个单词
print(s.split('.'))  # split()使用空白将字符串'.'作分隔符分割成多个短语

s3_list = s3.split()
print(s3_list)
print('/'.join(s3_list))  # join() 使用'/'将短语连接成字符串
