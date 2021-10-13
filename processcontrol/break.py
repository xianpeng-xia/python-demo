# 使用break终止循环

for i in range(0, 10):
    print('i = ', i)
    if i == 2:
        break
    else:
        print('else:', i)

#  嵌套循环，终止外层循环
exit_flag = False
for i in range(0, 5):
    for j in range(0, 3):
        print('i = %d , j = %d ' % (i, j))
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break
