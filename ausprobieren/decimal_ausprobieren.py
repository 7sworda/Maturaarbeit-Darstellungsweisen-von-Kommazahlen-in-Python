from decimal import *
from sys import getsizeof

print(getcontext())
a = Decimal("0.1")
print(getsizeof(a))
b = Decimal("0.2")
c = 0.1
print(a + b)
result = a / 7 * 1000000000
print(result)
print("length:" + str(len(str(result))))
print(getsizeof(result))
