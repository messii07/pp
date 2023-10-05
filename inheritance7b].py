class Shape:
    author = 'Ashwin Mehta'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def area(self):
        a = self.x * self.y
        print('Area of a rectangle:', a)
        print(Shape.author)


class Square(Shape):
    def __init__(self, x):
        self.x=x

    def area(self):
        a = self.x * self.x
        print('Area of a square:', a)
        print(Shape.author)


# Example usage
r = Rectangle(5, 4)
r.area()

s = Square(3)
s.area()
