class Polygon(object):
    def __init__(self, num, long):
        self.num = num
        self.long = long
        self.total = self.long * self.num
    def __str__(self):
        return f"[Polygon] 辺の数：　{self.num}, 辺の長さ：　{self.total}"

polygon1 = Polygon(4,4)
polygon2 = Polygon(5,1)

print(polygon1)
print(polygon2)