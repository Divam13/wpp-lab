from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width: {self.width}, height: {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle(radius: {self.radius})"

# Example usage:
rectangle = Rectangle(4, 5)
circle = Circle(3)

print(rectangle)
print(f"Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

print(circle)
print(f"Area: {circle.area()}, Perimeter: {circle.perimeter()}")
