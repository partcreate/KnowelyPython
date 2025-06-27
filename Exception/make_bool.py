from typing import Any

def from_int(value: Any) -> bool:
    if isinstance(value, int):
        if 0 <= value <= 1:
            return True if value == 1 else False
        else:
            raise ValueError
    else:
        raise TypeError


def from_str(value) -> bool:
    if isinstance(value, str):
        if value in ["True", "T", "1"]:
            return True
        elif value in ["False", "F", "0"]:
            print(value)
            return False
        else:
            raise ValueError
    else:
        raise TypeError


class BoolConversionError(Exception):
    pass


def make_bool(value) -> bool:
    if isinstance(value, bool):
        return value

    try:
        return from_int(value)
    except TypeError:
        pass
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")

    try:
        return from_str(value)
    except TypeError:
        raise BoolConversionError(f"Cannot convert to the bool {type(value).__name__} type")
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")


bool_value_1 = make_bool(1)
print(bool_value_1)  # True

bool_value_2 = make_bool("F")
print(bool_value_2)  # False

bool_value_3 = make_bool("false")
# BoolConversionError: Cannot convert to the bool false value

# bool_value_4 = make_bool({True})
# BoolConversionError: Cannot convert to the bool <class 'set'> type

def make_bool_2(value: Any) -> bool:
    try:
        return from_int(value)
    except TypeError:
        try:
            return from_str(value)
        except TypeError:
            raise BoolConversionError(f"Cannot convert to the bool {type(value)} type")
        except ValueError:
            raise BoolConversionError(f"Cannot convert to the bool {value} value")
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")


def make_bool_3(value: Any) -> bool:
    try:
        try:
            b = from_int(value)
        except TypeError:
            try:
                b = from_str(value)
            except TypeError:
                raise BoolConversionError(
                    f"Cannot convert to the bool {type(value)} type"
                )
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")
    else:
        return b
