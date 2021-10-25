# raise抛出异常
def main():
    try:
        mtd(3)
    except Exception as e:
        print("e = ",e)


def mtd(a):
    if a > 0:
        raise ValueError(">0")


main()
