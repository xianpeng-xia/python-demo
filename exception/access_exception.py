# 访问异常信息
def openFile():
    try:
        fis = open("a.txt")
    except Exception as e:
        # 访问异常的错误编码和详细信息
        print(e.args)
        # 访问异常的错误编码
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)
        # 访问传播轨迹信息
        print(e.with_traceback())


openFile()
