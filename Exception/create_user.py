class InvalidUsername(Exception):
    pass


def username_validation(username: str) -> None:
    if len(username) < 4 or len(username) > 14:
        raise InvalidUsername


class PasswordMismatch(Exception):
    pass


def password_validation(password1: str, password2: str) -> None:
    if password1 != password2:
        raise PasswordMismatch


class ValidationError(Exception):
    pass


def user_validation(user: dict[str, str]) -> None:
    try:
        username_validation(user["username"])
    except InvalidUsername:
        raise ValidationError

    try:
        password_validation(user["password1"], user["password2"])
    except PasswordMismatch:
        raise ValidationError


class DBUserCreationError(Exception):
    pass


def db_user_creation(user: dict[str, str]) -> None:
    try:
        user_validation(user)
    except (InvalidUsername, PasswordMismatch, ValidationError):
        raise DBUserCreationError
    else:
        print(f"{user["username"]} is created in the database.")


db_user_creation(
    user={"username": "User1",
          "password1": "password",
          "password2": "password"},
)

db_user_creation(
    user={"username": "User",
          "password1": "password",
          "password2": "password"},
)
#  DBUserCreationError
