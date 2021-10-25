#
import traceback


class SelfException(Exception): pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常")


try:
    main()
except:
    traceback.print_exc()
    traceback.print_exc(file=open('log.txt', 'a'))
