# 参数收集(可变参数),形参前面加'*'

def varargs_test(count, *books):
    print(type(books))
    print(books)
    for book in books:
        print(book)
    print(count)


varargs_test(2, "红楼梦", "三国演义")


# 可变参数可位于形参列表的任意位置,必须使用关键字参数给其他变量(只能有一个)赋值,
def varargs_test_2(cost, *books, count):
    print(type(books))
    print(books)
    for book in books:
        print(book)
    print(count)
    print(cost)


varargs_test_2("红楼梦", "三国演义", count=2)


# 一个函数可同时包含一个支持普通参数收集的参数(收集为元组)和一个支持关键字参数的参数(收集为字典)

def varargs_test_3(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


varargs_test_3(1, 2, 5, "语文书", "数学书", 语文=90, 数学=100)
# 参数z不能生效，除非books为空
varargs_test_3(1, 2, 语文=90, 数学=100)


# 逆向参数收集
def varargs_test_4(name, message):
    print("name = ", name)
    print("message = ", message)


my_list = ["Tome", "Hi"]
varargs_test_4(*my_list)


# 即使是支持收集的参数，如果需要将一个元组传给该参数，也需要逆向收集
def foo(name, *nums):
    print("name = ", name)
    print("nums = ", nums)


my_tuple = (1, 2, 4)
foo("Tom", *my_tuple)


# 字典也支持逆向收集

def bar(book, price, desc):
    print("book = ", book)
    print("price = ", price)
    print("desc = ", desc)


my_dict = {"price": 100, "book": "红楼梦", "desc": "四大名著之一"}
bar(**my_dict)