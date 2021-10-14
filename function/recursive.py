# 递归函数

# f(0) = 1,f(1)=4,f(n+2) = 2 * f(n + 1) + f(n)
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n - 1) + fn(n - 2)


print("f(10) = ", fn(10))
