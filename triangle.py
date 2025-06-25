from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height, side1=None, side2=None, side3=None):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__(base, height)
        self.name = "Triangle"
        self.side1 = side1 if side1 else base
        self.side2 = side2 if side2 else base
        self.side3 = side3 if side3 else (2 * base)  # fallback

    def get_area(self):
        return 0.5 * self.width * self.height

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3