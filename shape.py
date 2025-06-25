from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name="Shape"):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"{self.name} | Area: {self.get_area():.2f} | Perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return str(self)