# 查看类的父/子类
# __bases__属性：父类
# __subclasses__属性：子类
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print("A的所有父类", A.__bases__)
print("B的所有父类", B.__bases__)
print("C的所有父类", C.__bases__)

print("A的所有子类",A.__subclasses__())
print("B的所有子类",B.__subclasses__())