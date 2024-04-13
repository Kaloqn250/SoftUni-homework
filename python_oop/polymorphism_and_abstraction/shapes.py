from abc import abstractmethod, ABC
from cmath import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self) -> float:
        ...

    @abstractmethod
    def calculate_perimeter(self) -> float:
        ...


class Circle(Shape):

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Shape):

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.height + self.width)



circle = Circle(5)

print(circle.calculate_area())

print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)

print(rectangle.calculate_area())

print(rectangle.calculate_perimeter())
