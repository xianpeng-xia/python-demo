# 多异常捕获
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("c = ", c)
except (IndexError, ValueError, AttributeError):
    print("IndexError | ValueError | AttributeError ")

except Exception:
    print("Exception")
