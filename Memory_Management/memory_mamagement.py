import copy


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Triangle:
    def __init__(self, first_point: Point, second_point: Point, third_point: Point) -> None:
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def __str__(self) -> str:
        return (f"Triangle out of ({self.first_point.x}, {self.first_point.y}), "
                f"({self.second_point.x}, {self.second_point.y}), "
                f"({self.third_point.x}, {self.third_point.y})")


def copy_point(point: Point) -> Point:
    return copy.copy(point)


def copy_triangle(triangle: Triangle) -> Triangle:
    return copy.deepcopy(triangle)


point_a = Point(x=1, y=1)
triangle_a = Triangle(
    first_point=Point(x=0, y=0),
    second_point=Point(x=1, y=3),
    third_point=Point(x=5, y=5)
)
copied_triangle = copy_triangle(triangle_a)

print(triangle_a is copied_triangle)  # False
print(triangle_a.first_point is copied_triangle.first_point)  # False

point_b = Point(x=1, y=1)
print(point_b)  # Point(1, 1)

triangle_b = Triangle(
    first_point=Point(x=0, y=0),
    second_point=Point(x=1, y=3),
    third_point=Point(x=5, y=5)
)
print(triangle_b)  # Triangle out of (0, 0), (1, 3) ,(5, 5)
