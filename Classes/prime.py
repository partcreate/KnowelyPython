from __future__ import annotations
import math
from typing import Any, Generator


class LowerPrime:
    def __init__(self, number: int) -> None:
        self.number = number

        self.prime_cache = self.prime_generator(self.number)

    def __iter__(self) -> LowerPrime:
        return self

    def __next__(self) -> int:

        prime_num = next(self.prime_cache)

        print("prime_num: ", prime_num)

        if prime_num < 2:
            raise StopIteration
        else:
            return prime_num

    def check_prime(self, num: int) -> bool:

        if num < 2:
            return False

        if num == 2:
            return True

        if num % 2 == 0:
            return False

        limit = int(math.sqrt(num)) + 1

        for i in range(3, limit, 2):
            if num % i == 0:
                return False

        return True

    def prime_generator(self, num: int) -> Generator[int, Any, None]:

        if num <= 2:
            return

        for i in range(num - 1, 0, -1):
            print("i: ", i)
            if self.check_prime(i):
                yield i
