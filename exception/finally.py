# finally回收资源
import os


def open_file():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as e:
                print(e.strerror)
        print("finally...")


open_file()
