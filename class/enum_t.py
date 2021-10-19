from enum import Enum

# 使用Enum列出多个枚举值来创建枚举类
Season = Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
print(Season.SPRING)

print(Season.WINTER.name)
print(Season.WINTER.value)

# 根据枚举变量名访问
print(Season['FALL'])
# 根据枚举值访问
print(Season(2))

# _member_map_属性返回一个字典，包含了该枚举的所有枚举实例
for name, member in Season._member_map_.items():
    print(name, '->', member, ',', member.value)
