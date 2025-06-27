from typing import Callable


def html_tag(tag: str) -> str:
    def decorator(func: Callable) -> Callable:
        def wrapper(name: str) -> str:
            get_name = func(name)
            return f"<{tag}>{get_name}</{tag}>"

        return wrapper

    return decorator


@html_tag("p")
def greeter(name: str) -> str:
    return f"Hello, {name}!"

@html_tag('div')
def greeter(name: str) -> str:
    return f"Hello, {name}!"

print(greeter('Alex'))

@html_tag('p')
@html_tag('a')
def greeter(name: str) -> str:
    return f"Hello, {name}!"

print(greeter('Maxim'))