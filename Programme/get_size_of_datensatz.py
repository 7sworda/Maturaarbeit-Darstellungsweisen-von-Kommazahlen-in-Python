import csv
from sys import getsizeof, set_int_max_str_digits, maxsize
from decimal import Decimal
from fractions import Fraction

csv.field_size_limit(maxsize)
set_int_max_str_digits(131074) # Increase Python's limit for converting large integer strings, which is required for constructing Fractions from the dataset
with open('datensatz.csv', newline='') as dataset, open('speicheraufwand_der_zahlenobjekte.csv', mode='w', newline='') as resultfile:
    datareader = csv.reader(dataset, dialect='excel', delimiter=';')
    datawriter = csv.writer(resultfile, dialect='excel', delimiter=';')
    
    for numberpair in datareader:
        a, b = numberpair[1], numberpair[2]
        
        a_float = float(a)
        b_float = float(b)
        
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        
        a_fraction = Fraction(a)
        b_fraction = Fraction(b)
        
        a_float_size = getsizeof(a_float)
        b_float_size = getsizeof(b_float)
        
        a_decimal_size = getsizeof(a_decimal)
        b_decimal_size = getsizeof(b_decimal)
        
        # getsizeof() only measures the Fraction object itself,
        # so the sizes of the numerator and denominator must be added separately
        a_fraction_size = getsizeof(a_fraction) + getsizeof(a_fraction.numerator) + getsizeof(a_fraction.denominator)
        b_fraction_size = getsizeof(b_fraction) + getsizeof(b_fraction.numerator) + getsizeof(b_fraction.denominator)
        
        datawriter.writerows([[a_float_size, a_decimal_size, a_fraction_size],
                              [b_float_size, b_decimal_size, b_fraction_size]])
    
    