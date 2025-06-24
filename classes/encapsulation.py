class PublicBase:
    def __init__(self):
        self.public = "public"

    def print_info(self):
        print(f"{self.public} attribute")


class PublicDerived(PublicBase):
    def __init__(self):
        super().__init__()
        print(self.public)


public_base = PublicBase()

print(public_base.public)        # public
public_base.print_info()         # public attribute


class ProtectedBase:
    def __init__(self):
        self._protected = "protected"

    def print_info(self):
        print(f"{self._protected} attribute")


class ProtectedDerived(ProtectedBase):
    def __init__(self):
        super().__init__()
        print(self._protected)


protected_base = ProtectedBase()

print(protected_base._protected)        # protected
protected_base.print_info()             # protected attribute


class PrivateBase:
    def __init__(self):
        self.__private = "private"

    def __print_info(self):
        print(f"{self.__private} attribute")


class PrivateDerived(PrivateBase):
    def __init__(self):
        super().__init__()
        print(self.__private)


private_base = PrivateBase()

print(private_base._PrivateBase__private) # private
print(private_base.__private) # Error
private_base.__print_info() # Error
PrivateDerived()  # Error
