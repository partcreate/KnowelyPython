from typing import Any


class Grade:
    def __init__(self) -> None:
        self.minvalue = 2
        self.maxvalue = 12

    def __set_name__(self, owner: Any, name: str):
        self.public_name = name
        self.protected_name = "_" + name

    def __get__(self, instance: Any, owner: Any) -> int:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")

        if value < self.minvalue or value > self.maxvalue:
            raise ValueError(f"Grade should not be less than {self.minvalue}"
                             f" and greater than {self.maxvalue}")

        setattr(instance, self.protected_name, value)


class SchoolDiary:

    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math: int, history: int, literature: int) -> None:
        self.math = math
        self.history = history
        self.literature = literature


# alex = SchoolDiary(math="10", history="12", literature="9")
# TypeError: Grade should be integer

# nina = SchoolDiary(math=15, history=12, literature=9)
# ValueError: Grade should not be less than 2 and greater than 12

berit = SchoolDiary(math=5, history=8, literature=9)

print(berit.math)
print(berit.history)
print(berit.literature)