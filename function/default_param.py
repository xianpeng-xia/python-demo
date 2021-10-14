# 参数默认值

def say_hi(name='Tom', message="欢迎！！！"):
    print(name, " , Hi")
    print("msg : ", message)


# 全部使用默认参数
say_hi()
# message会使用默认值
say_hi("Bob")
# 都不使用默认参数
say_hi("Lisa", "Hello")
# 只有name使用默认参数
say_hi(message="Welcome")


# 有默认值的参数必须放在最后

def printTriangle(char, height=5):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print(char, end='')
        print()


printTriangle("@", 6)
printTriangle("*", 7)
printTriangle(char="&")
