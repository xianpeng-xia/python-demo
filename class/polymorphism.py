# 多态
class Canvas:
    def draw_pic(self, shape):
        print("开始画图")
        shape.draw(self)


class Rectangle:
    def draw(self, canvas):
        print("在%s上画矩形" % canvas)


class Triangle:
    def draw(self, canvas):
        print("在%s上画三角形" % canvas)


class Circle:
    def draw(self, canvas):
        print("在%s上画圆形" % canvas)


c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())
