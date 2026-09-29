import csv
import sys
from timeit import Timer

def avg_time(iterations: int, total_time: float)-> float:
    return total_time/iterations

csv.field_size_limit(sys.maxsize)

with open('datensatz.csv', newline='') as dataset, open('laufzeit_subtraktion.csv', mode='a', newline='') as resultfile:
    datareader = csv.reader(dataset, dialect='excel', delimiter=';')
    datawriter = csv.writer(resultfile, dialect='excel', delimiter=';')
    
    for numberpair in datareader:
        a, b = numberpair[1], numberpair[2]
        
        float_time = avg_time(*Timer("a-b", setup=f"a = float(\"{a}\"); b = float(\"{b}\")").autorange())
        decimal1_time = avg_time(*Timer("a-b", setup=(
            f"from decimal import Decimal, setcontext, Context;"
            f"setcontext(Context(prec=16, Emax=384, Emin=-383, traps=[]));"
            f"a = Decimal(\"{a}\") + 0; b = Decimal(\"{b}\") + 0")).autorange())
        decimal2_time = avg_time(*Timer("a-b", setup=(
            f"from decimal import Decimal, setcontext, Context, MAX_PREC, MIN_EMIN, MAX_EMAX;"
            f"setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[]));"
            f"a = Decimal(\"{a}\"); b = Decimal(\"{b}\")")).autorange())
        fraction_time = avg_time(*Timer("a-b", setup=(
            f"from fractions import Fraction;"
            f"from sys import set_int_max_str_digits;"
            f"set_int_max_str_digits(131074);"
            f"a = Fraction(\"{a}\"); b = Fraction(\"{b}\")")).autorange())
        
        datawriter.writerow([float_time, decimal1_time, decimal2_time, fraction_time])
        
        
    
