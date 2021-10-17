# 类的类方法和静态方法

class Bird:
    @classmethod
    def fly(cls):
        print("类方法fly")

    @staticmethod
    def info(p):
        print("静态方法info:", p)


Bird.fly()
Bird.info("Hello")

# 使用对象调用，其实依然还是使用类调用的
b = Bird()
b.fly()
b.info("Hi")
