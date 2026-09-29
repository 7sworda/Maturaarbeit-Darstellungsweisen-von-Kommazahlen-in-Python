from decimal import *
from sys import getsizeof

a = 0.1
b = Decimal("0.1")
getcontext().prec = 256
c = Decimal(1) / Decimal(7)
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))