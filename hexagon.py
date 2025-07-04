from shape import Shape
from math import sqrt

class Hexagon(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive.")
        self.side = side
        super().__init__("Hexagon")

    def get_area(self):
        return ((3 * sqrt(3)) / 2) * self.side ** 2

    def get_perimeter(self):
        return 6 * self.side