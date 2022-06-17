import fractions
import decimal


a = fractions.Fraction(1, 5)
print(a)
a += 5
print(a)

print(a.numerator)
print(a.denominator)

# a3 = fractions.Fraction(1, 3)
a3 = fractions.Fraction(1, 7)
print(a3)
print(float(a3))
print(decimal.Decimal(1) / decimal.Decimal(3))



