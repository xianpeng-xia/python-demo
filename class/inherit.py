# 继承

class Fruit:
    def info(self):
        print("我是一个水果，重%g克" % self.weight)


class Food:
    def taste(self):
        print("不同食物的口感不同")


# ()里为父类
class Apple(Fruit, Food):
    pass


a = Apple()
a.weight = 5
a.info()
a.taste()
