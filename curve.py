class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class ElipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p  # mod p

    def addition(self, p1, p2):
        if p2 == Point(0, 0):
            print("P1 + P2 = ", "(", p1.x, ",", p1.y, ")")
        if p1 == Point(0, 0):
            print("P1 + P2 = ", "(", p2.x, ",", p2.y, ")")
        if p1 == p2:
            l = (3 * p1.x**2 + self.a) / (2 * p1.y) % self.p
        else:
            l = (p2.y - p1.y) / (p2.x - p1.x) % self.p
            pass


p1 = Point(0, 0)
p2 = Point(0, 0)
ec = ElipticCurve(3, 8, 13)

print(ec.addition(p1, p2))
