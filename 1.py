import math
class Polygon(object):
    def __init__(self, n, l):
        self.edges = n
        self.length = l

    def __str__(self):
        return f"[Polygon] 辺の数: {self.edges:d}, 辺の長さ: {self.length:d}"

    def perimeter(self):
        return self.edges * self.length


class Triangle(Polygon):
    def __init__(self, length):
        super().__init__(3, length)
    def area(self):
        height = math.sqrt(3) * self.length / 2
        return height * self.length / 2
class Square(Polygon):
    def __init__(self, length):
        super().__init__(4, length)
    def area(self):
        return self.length ** 2
triangle = Triangle(10)
print(triangle)
print("周囲の長さ:", triangle.perimeter())
print("面積:", triangle.area())

square = Square(25)
print(square)
print("周囲の長さ:", square.perimeter())
print("面積:", square.area())