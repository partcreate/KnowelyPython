from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self):
        super().__init__("triangle")
        print(self.__class__.__name__)

    def draw(self):
        print("Drawing a triangle")


triangle = Triangle()
triangle.draw()			# Drawing a triangle


class Machine(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def do_work(self) -> None:
        pass

    @abstractmethod
    def stop_work(self) -> None:
        pass


class Truck(Machine):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def do_work(self) -> None:
        print(f"{self.name} starts working")

    def stop_work(self) -> None:
        print(f"{self.name} stopped working")


class Bulldozer(Machine):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def do_work(self) -> None:
        print(f"{self.name} starts working")

    def stop_work(self) -> None:
        print(f"{self.name} stopped working")


class Excavator(Machine):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def do_work(self) -> None:
        print(f"{self.name} starts working")

    def stop_work(self) -> None:
        print(f"{self.name} stopped working")


def build() -> None:
    machines = [Truck(), Bulldozer(), Excavator()]

    for machine in machines:
        machine.do_work()

    for machine in machines:
        machine.stop_work()

build()