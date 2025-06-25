from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

def main():
    shapes = []

    try:
        shapes.append(Rectangle(3, 4))
        shapes.append(Square(5))
        shapes.append(Triangle(6, 3, 6, 5, 4))
        shapes.append(Circle(7))
        shapes.append(Hexagon(2.5))
    except ValueError as e:
        print("Error creating shape:", e)

    for shape in shapes:
        print(shape)

if __name__ == "__main__":
    main()
