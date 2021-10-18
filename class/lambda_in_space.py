# 全局空间的lambda表达式
global_fn = lambda p: print("param: ", p)


class Category:
    # 自动绑定第一个参数
    cate_fn = lambda p: print("param: ", p)


global_fn("a")

c = Category()
c.cate_fn()
