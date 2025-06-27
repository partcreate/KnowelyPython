from decimal import Decimal
from typing import Any


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


def deci_mal(num: Any) -> int:

    if isinstance(num, int):
        return 0
    try:
        d = Decimal(str(num))
        return -d.as_tuple().exponent if d.as_tuple().exponent < 0 else 0
    except Exception:
        return 0


print(deci_mal(1e-05))
