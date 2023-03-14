class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_Area(self):
        return self.width * self.length


rect = Rectangle(2, 3)
print(f"Your rectangle length is {rect.length}")
print(f"Your rectangle width is {rect.width}")
print(f"Your rectangle area is {rect.rectangle_Area()}")
