from typing import Callable, Any


def composition(first_function: Callable, second_function: Callable) -> Callable:
    def res_func(*args, **kwargs) -> Any:
        return first_function(second_function(*args, **kwargs))

    return res_func


first_func = lambda a: 2 * a + 3  # 2 * 5 + 3 = 13
second_func = lambda a, b: a + b  # 2 + 3 = 5
print(composition(first_func, second_func)(2, 3))  # returns 13