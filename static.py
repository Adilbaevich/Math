import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def S(self):
        return math.pi * (self.radius ** 2)

    def P(self):
        return 2 * math.pi * self.radius

class Square():
    def __init__(self,a):
        self.a = a

    def S(self):
        return self.a**2

    def P(self):
        return 4*self.a

class Rectangle():
     def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

     def S(self):
        return (self.a * self.b)/2

     def P(self):
        return self.a + self.b + self.c


circle = Circle(4)
print("S: ", circle.S())
print("P: ", circle.P())

square = Square(5)
print("S: ", square.S())
print("P: ", square.P())

rectangle = Rectangle(3,4,5)
print("S: ", rectangle.S())
print("P: ", rectangle.P())