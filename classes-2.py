class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        return self.length**2

x=Shape()
print("Area of shape:", x.area())

y=Square(4)
print("Area of square:", y.area())


