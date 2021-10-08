# 1 Byte = 8 bit
# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytesz值
b2 = b''
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2: 4])
# 调用bytes()方法将字符串转化为bytes对象
b4 = bytes('我爱Python编程', encoding='utf-8')
print(b4)
# 使用字符串的encode()方法编码成bytes
b5 = "学习Python很有趣".encode('utf-8')
print(b5)

# 将Bytes转成字符串
st = b5.decode('utf-8')
print(st)
