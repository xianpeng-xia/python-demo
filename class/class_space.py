# 全局空间的foo函数
def foo():
    print("全局空间的foo方法")


# 全局空间的bar变量
bar = 20


class Bird:
    # Bird空间的foo函数
    def foo(self):
        print("Bird空间的foo方法")

    # Bird空间的bar变量
    bar = 200


foo()
print(bar)

b = Bird()
print(Bird.foo(b))
print(Bird.bar)
