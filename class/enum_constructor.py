# 枚举构造器
import enum


class Gender(enum.Enum):
    MALE = '男', '阳刚'
    FEMALE = '女', '阴柔'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


print(Gender.FEMALE.name)
print(Gender.FEMALE.value)
print(Gender.FEMALE.cn_name)
print(Gender.FEMALE.desc)
