import math
class Shape:
 
    def S(self):
        pass

    def P(self):
        pass

class Square(Shape):
    def __init__(self,a):
        self.a = a

    def S(self):
        return self.a**2

    def P(self):
        return 4*self.a

class Rectangle(Shape):
     def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

     def S(self):
        return (self.a * self.b)/2

     def P(self):
        return self.a + self.b + self.c

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def S(self):
        return math.pi * (self.radius ** 2)

    def P(self):
        return 2 * math.pi * self.radius

square = Square(5)
print("S: ", square.S())
print("P: ", square.P())

rectangle = Rectangle(3,4,5)
print("S: ", rectangle.S())
print("P: ", rectangle.P())

circle = Circle(4)
print("S: ", circle.S())
print("P: ", circle.P())