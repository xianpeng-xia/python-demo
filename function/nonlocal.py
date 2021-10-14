# nonlocal 声明访问赋值语句只是访问该函数所在函数内的局部变量

def foo():
    name = 'Tom'

    def bar():
        nonlocal name
        print(name)
        name = "Lias"

    bar()
    print(name)


foo()
