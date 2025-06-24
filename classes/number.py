import math


class NumberInfo:
    def __init__(self, number: int | float) -> None:
        self.number = number
        """
        len_digits: int,
        is_integer: bool,
        is_float: bool,
        decimal: int,
        is_positiv: bool,
        is_natural: bool,
        is_prime: bool
        """

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def len_digits(self) -> int:
        print(self._number)
        length = len(str(abs(int(self._number))))
        print(length)
        return length

    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int)

    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float)

    @property
    def decimal(self) -> int:
        return len(str(self._number).split(".")[1]) if self.is_float else 0

    @property
    def is_positive(self) -> bool:
        return self._number > 0

    @property
    def is_natural(self) -> bool:
        return self.is_integer and self.is_positive

    @property
    def is_prime(self) -> bool:
        if self.is_float:
            return False

        if self._number < 2:
            return False

        if self._number == 2:
            return True

        if self._number % 2 == 0:
            return False

        limit = int(math.sqrt(self._number)) + 1

        for i in range(3, limit, 2):
            if self._number % i == 0:
                return False

        return True


number_int = NumberInfo(1e-05)

test_int = [number_int.number,
number_int.len_digits,
number_int.is_integer,
number_int.is_float,
number_int.decimal,
number_int.is_positive,
number_int.is_natural,
number_int.is_prime
]

print(test_int)
