from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return self.r**2*pi

    @property
    def perimeter(self):
        return 2*pi*self.r

c = Circle(10)
print(c.area)
print(c.perimeter)
c.r = 15
print(c.area)
print(c.perimeter)