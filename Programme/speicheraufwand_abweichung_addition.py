import csv
import tracemalloc
from sys import getsizeof, set_int_max_str_digits, maxsize
from decimal import Decimal, setcontext, Context, MAX_PREC, MIN_EMIN, MAX_EMAX
from fractions import Fraction
from math import isinf

def trace_memory(a, b):
    tracemalloc.start()

    c = a + b

    traced_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return traced_memory[1], c

def size_of(c):
    if isinstance(c, Fraction):
        return getsizeof(c) + getsizeof(c.numerator) + getsizeof(c.denominator)
    else:
        return getsizeof(c)
    
def deviation(c, reference):
    if isinf(c):
        return ""
    else:
        calculated_deviation = abs(reference - Fraction(c))/abs(reference)
        return f"{calculated_deviation:.14E}"

csv.field_size_limit(maxsize)
set_int_max_str_digits(131074)

decimal1_context = Context(prec=16, Emin=-383, Emax=384, traps=[])
decimal2_context = Context(prec=MAX_PREC, Emin=MIN_EMIN, Emax=MAX_EMAX)

with open('datensatz.csv', newline='') as dataset, open('höchster_speicheraufwand_addition.csv', mode='w', newline='') as maxmemoryfile, open('speicheraufwand_des_resultats_addition.csv', mode='w', newline='') as resultsizefile, open('abweichung_addition.csv', mode='w', newline='') as deviationfile:
    datareader = csv.reader(dataset, dialect='excel', delimiter=';')
    datawriter_maxmemory = csv.writer(maxmemoryfile, dialect='excel', delimiter=';')
    datawriter_resultsize = csv.writer(resultsizefile, dialect='excel', delimiter=';')
    datawriter_deviation = csv.writer(deviationfile, dialect='excel', delimiter=';')
    
    for numberpair in datareader:
        a, b = numberpair[1], numberpair[2]
        
        a_fraction = Fraction(a)
        b_fraction = Fraction(b)
        
        fraction_maxmemory, reference = trace_memory(a_fraction, b_fraction)
        fraction_resultsize = size_of(reference)
        fraction_deviation = 0
        
        a_float = float(a)
        b_float = float(b)
        
        float_maxmemory, float_result = trace_memory(a_float, b_float)
        float_resultsize = size_of(float_result)
        float_deviation = deviation(float_result, reference)
        
        setcontext(decimal1_context)
        a_decimal1 = Decimal(a) + 0 # Addition with 0 applies the current context precision to the Decimal value
        b_decimal1 = Decimal(b) + 0
        
        decimal1_maxmemory, decimal1_result = trace_memory(a_decimal1, b_decimal1)
        decimal1_resultsize = size_of(decimal1_result)
        decimal1_deviation = deviation(decimal1_result, reference)
        
        setcontext(decimal2_context)
        a_decimal2 = Decimal(a)
        b_decimal2 = Decimal(b)
        
        decimal2_maxmemory, decimal2_result = trace_memory(a_decimal2, b_decimal2)
        decimal2_resultsize = size_of(decimal2_result)
        decimal2_deviation = deviation(decimal2_result, reference)
        
        datawriter_maxmemory.writerow([float_maxmemory, decimal1_maxmemory, decimal2_maxmemory, fraction_maxmemory])
        datawriter_resultsize.writerow([float_resultsize, decimal1_resultsize, decimal2_resultsize, fraction_resultsize])
        datawriter_deviation.writerow([float_deviation, decimal1_deviation, decimal2_deviation, fraction_deviation])



