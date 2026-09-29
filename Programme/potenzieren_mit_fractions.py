from fractions import Fraction

a = Fraction("2")
b = Fraction("4")
c = Fraction("0.5")
d = a ** c # Wurzel von 2
e = b ** c # Wurzel von 4
f = a ** 2 # Quadrat von 2

print(d) # 1.4142135623730951
print(type(d)) # <class 'float'>
print(e) # 2.0
print(type(e)) # <class 'float'>
print(f) # 4
print(type(f)) # <class 'fractions.Fraction'>
