# 使用super函数调用父类的构造方法
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print("我是一名员工，工资是:", self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print("我是一个顾客，爱好是%s，地址是%s" % (self.favorite, self.address))


class Manager(Employee, Customer):
    def __init__(self, salary, favorite, address):
        print("Manager的构造方法")
        super().__init__(salary)
        # 与上一行效果相同
        # super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类的构造器
        Customer.__init__(self, favorite, address)


m = Manager(30000, "NBA", "北京")
m.work()
m.info()
