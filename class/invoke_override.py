# 通过未绑定方法显式调用父类方法
class BaseClass:
    def foo(self):
        print("父类的foo方法")


class SubClass(BaseClass):
    def foo(self):
        print("子类的foo方法")

    def bar(self):
        print("bar方法")
        self.foo()
        # 通过未绑定方法显式调用父类方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()
