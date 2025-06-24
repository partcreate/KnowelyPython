from decimal import Decimal

a_1 = Decimal(0)
a_2 = Decimal(1)
a_3 = Decimal(2.345)
a_4 = Decimal(1e-05)

print(a_1)
print(a_2)
print(a_3)
print(a_4)

number = 1.234
str_num = f"{number:.15f}".rstrip("0")
print(Decimal.from_float(1e-05))
print(str_num)
