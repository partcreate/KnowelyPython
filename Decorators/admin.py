from typing import Callable, Any


class UnauthenticatedError(Exception):
    pass


def login_required(func: Callable) -> Any:
    def wrapper(request: dict) -> None:
        print(request)
        if request.get("user") is None:
            raise UnauthenticatedError("Authentication credentials were not provided!")
        else:
            func(request)

    return wrapper


class PermissionDeniedError(Exception):
    pass


def admin_required(func: Callable) -> Any:
    def wrapper(request: dict) -> None:
        print(request)
        if request["user"]["is_admin"] is False:
            raise PermissionDeniedError("User must be admin!")
        else:
            func(request)

    return wrapper


@login_required
@admin_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request['user']['full_name']}")


request_1 = {"user": {"full_name": "James Bond", "is_admin": True}}
access_admin_page(request_1)
# Welcome to the admin page, James Bond

request_2 = {"user": {"full_name": "John Smith", "is_admin": False}}
access_admin_page(request_2)
# PermissionDeniedError: User must be admin!

request_3 = {}
access_admin_page(request_3)
# UnauthenticatedError: Authentication credentials were not provided!
