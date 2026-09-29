from random import randint
from fractions import Fraction
from decimal import Decimal, setcontext, Context, MAX_PREC, MIN_EMIN, MAX_EMAX
from sys import getsizeof, set_int_max_str_digits
from datetime import datetime
import tracemalloc

startTime = datetime.now()
set_int_max_str_digits(2000000000)
setcontext(Context(prec=2**18, Emax=MAX_EMAX, Emin=MIN_EMIN))

def trace_multiplication_memory(a, b):
    tracemalloc.start()

    c = a / b

    traced_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return traced_memory + (getsizeof(c), c)

n = 18

a = randint(2**(2**n-1), 2**(2**n)-1)
b = randint(2**(2**n-1), 2**(2**n)-1)
a_exp = randint(0, 2**n)
b_exp = randint(0, 2**n)

a_float = float(f"{a}")
b_float = float(f"{b}")
a_decimal = Decimal(a) * (2**a_exp)
b_decimal = Decimal(b) * (2**b_exp)
a_fraction = Fraction(a) * (2**a_exp)
b_fraction = Fraction(b) * (2**b_exp)

print(trace_multiplication_memory(a, b)) #current size, peak size, result
print(trace_multiplication_memory(a_float, b_float))
a_decimal_memory, a_decimal_memory_peak, decimal_result_size, decimal_result = trace_multiplication_memory(a_decimal, b_decimal)
print((a_decimal_memory, a_decimal_memory_peak, decimal_result_size, decimal_result))
a_fraction_memory, a_fraction_memory_peak, fraction_result_size, fraction_result = trace_multiplication_memory(a_fraction, b_fraction)
print((a_fraction_memory, a_fraction_memory_peak, fraction_result_size, fraction_result))
print(f"{(fraction_result-Fraction(decimal_result)) / fraction_result:*>20.6e}") #relative Abweichung
print(datetime.now() - startTime)
