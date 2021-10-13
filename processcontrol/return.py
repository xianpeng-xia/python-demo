# return

def test():
    for i in range(10):
        for j in range(10):
            print('i = %d , j = %d' % (i, j))
            if j == 1:
                return


test()
