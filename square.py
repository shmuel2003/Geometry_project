from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive.")
        super().__init__(side, side)
        self.name = "Square"