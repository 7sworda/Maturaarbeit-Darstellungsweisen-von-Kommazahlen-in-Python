from decimal import Decimal, setcontext, Context
from sys import getsizeof

setcontext(Context(prec=16, Emax=1, Emin=-1))

a = Decimal(1) / 7
print(a)
b = Decimal()
print(getsizeof(a))