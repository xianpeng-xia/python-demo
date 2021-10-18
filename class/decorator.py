# @函数装饰器

def funA(fn):
    print('A')
    fn()  # 执行输入的fn参数
    return 'RA'


# 相当与funA(funB)
# funB将会被替换(装饰)成该语句的返回值，即 funB 就是 'RA'
@funA
def funB():
    print('B')


print(funB)


# ------复杂的函数装饰器
def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("====1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))

    return bar


@foo
def my_test(a):
    print("===my_test===", a)


print(my_test)
my_test(10)
my_test(6, 5)


# ---Aop
def auth(fn):
    def auth_fn(*args):
        print("---auth check---")
        fn(*args)

    return auth_fn


@auth
def test(a, b):
    print("a = %s , b = %s" % (a, b))


test(5, 6)
