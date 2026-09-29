from random import seed, randint
from timeit import timeit, Timer

a = randint(2**1, 2**2-1)
b = randint(2**1, 2**22-1)

timed1 = Timer("a*b", setup=(
    f"from fractions import Fraction;"
    f"a = Fraction({a}); b = Fraction({b})")).autorange()
timed2 = Timer("a*b", setup=f"from decimal import Decimal; a = Decimal({a}); b = Decimal({b})").autorange()
timed3 = Timer("a*b", setup=f"a = float({a}); b = float({b})").autorange()

def avg_time(number, time_taken):
    return time_taken/number

print(a, b)
print(timed1)
print(avg_time(*timed1))
print(timed2)
print(avg_time(*timed2))
print(timed3)
print(avg_time(*timed3))