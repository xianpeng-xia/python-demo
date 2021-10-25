# 当try中没有异常，执行else块
def else_func():
    s = input("除数 : ")
    result = 20 / int(s)
    print("result = ", result)


def right_main():
    try:
        print("try代码块无异常")
    except Exception as e:
        print(e.strerror())
    else:
        else_func()


def wrong_main():
    try:
        print("try代码块无异常")
        else_func()

    except Exception as e:
        print(e.strerror())


wrong_main()
right_main()
