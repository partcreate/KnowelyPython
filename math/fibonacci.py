from typing import Any, Generator


def fibonacci_number(num_index: int) -> int:

    a, b = 0, 1

    for i in (range(num_index)):
        a, b = b, a + b

    return a

def fibonacci_generator(num_index: int) -> Generator[int | Any, Any, None]:
    a, b = 0, 1
    for i in range(num_index):
        yield a
        a, b = b, a + b