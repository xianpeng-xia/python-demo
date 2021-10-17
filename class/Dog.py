# self参数在普通实例方法中引用调用该方法的对象
class Dog:
    def jump(self):
        print("jump...")

    def run(self):
        self.jump()
        print("run...")
