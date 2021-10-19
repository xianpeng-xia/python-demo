import enum


# 继承Enum派生出枚举类
class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print("方向为%s" % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)

print(Orientation['WEST'])
# 可通过value来访问
print(Orientation('南'))
Orientation.WEST.info()
