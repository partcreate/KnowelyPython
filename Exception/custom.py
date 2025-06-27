from typing import Any


class CanRideExtremeException(Exception):
    min_age = 18
    max_age = 45

    def __init__(self, age, *args):
        super().__init__(args)
        self.age = age

    def __str__(self):
        return f"The age {self.age} is not in a valid range {self.min_age} - {self.max_age}."


def can_ride(age: int) -> bool:
    if (age <= CanRideExtremeException.min_age) or (
        age >= CanRideExtremeException.max_age
    ):
        raise CanRideExtremeException(age)
    return True


print(can_ride(27))  # True
print(can_ride(12))
# __main__.CanRideExtremeException: The age 12 is not in a valid range 18 - 45.



# 1. Definiere eine benutzerdefinierte Ausnahme (Exception)
#    Diese Klasse erbt von ValueError (oder einer anderen passenden Exception).
#    Sie ist KEIN Descriptor.
class InvalidRangeError(ValueError):
    """
    Ausnahme, die ausgelöst wird, wenn ein Wert außerhalb des erwarteten Bereichs liegt.
    """

    def __init__(self, message: str, value: Any, min_val: Any, max_val: Any):
        super().__init__(message)
        self.value = value
        self.min_val = min_val
        self.max_val = max_val

    def __str__(self):
        return (f"Fehler: {super().__str__()}. Der Wert {self.value} liegt nicht "
                f"zwischen {self.min_val} und {self.max_val}.")


# 2. Definiere den Descriptor, der die Ausnahme auslöst
#    Diese Klasse ist ein Descriptor. Sie ist KEINE Exception.
class IntegerRange:
    """
    Ein Descriptor, der sicherstellt, dass ein Integer-Wert innerhalb eines Bereichs liegt.
    Löst InvalidRangeError aus, wenn die Validierung fehlschlägt.
    """

    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner: Any, name: str):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance: Any, owner: Any) -> int:
        if instance is None:
            return self
        if hasattr(instance, self.private_name):
            return getattr(instance, self.private_name)
        raise AttributeError(f"Attribut '{self.public_name}' wurde für diese Instanz nicht gesetzt.")

    def __set__(self, instance: Any, value: int):
        if not isinstance(value, int):
            raise TypeError(
                f"'{self.public_name}' muss ein Integer sein, aber '{value}' ist vom Typ {type(value).__name__}.")

        # HIER WIRD DIE AUSNAHME AUSGELÖST
        if not (self.min_val <= value <= self.max_val):
            raise InvalidRangeError(
                f"Wert außerhalb des zulässigen Bereichs für '{self.public_name}'",
                value=value,
                min_val=self.min_val,
                max_val=self.max_val
            )

        setattr(instance, self.private_name, value)

    def __delete__(self, instance: Any):
        if not hasattr(instance, self.private_name):
            raise AttributeError(f"'{self.public_name}' wurde nicht gesetzt und kann nicht gelöscht werden.")
        delattr(instance, self.private_name)


class Person:
    alter = IntegerRange(0, 120)  # Person.alter ist jetzt ein Descriptor

    def __init__(self, name: str, age: int):
        self.name = name
        self.alter = age  # Dies löst den Setter des 'alter'-Descriptors auf


# --- Nutzung mit Fehlerbehandlung ---
print("--- Person erstellen (gültig) ---")
try:
    p1 = Person("Alice", 30)
    print(f"Person {p1.name} erfolgreich erstellt, Alter: {p1.alter}")
except (TypeError, ValueError, InvalidRangeError) as e:
    print(f"Fehler bei Erstellung: {e}")

print("\n--- Person erstellen (Alter außerhalb des Bereichs) ---")
try:
    p2 = Person("Bob", 150)  # Alter außerhalb des Bereichs
except InvalidRangeError as e:  # Fange die spezifische benutzerdefinierte Ausnahme ab
    print(f"Fehler abgefangen (InvalidRangeError): {e}")
except (TypeError, ValueError) as e:
    print(f"Anderer Fehler abgefangen: {e}")

print("\n--- Person erstellen (falscher Typ) ---")
try:
    p3 = Person("Charlie", "dreißig")  # Falscher Typ
except TypeError as e:  # Fange den spezifischen TypeError ab
    print(f"Fehler abgefangen (TypeError): {e}")

