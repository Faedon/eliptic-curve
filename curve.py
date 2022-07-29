from cmath import e


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class EllipticCurve:
    def __init__(self, a, b, p, n):
        self.a = a
        self.b = b
        self.p = p  # mod p
        self.n = n

    def inv_mod_p(self, x):
        if x % self.n == 0:
            raise ZeroDivisionError("Impossible inverse")
        return pow(x, self.n - 2, self.n)

    def add(self, p1, p2):
        if p2 == Point(0, 0):
            result = p1
        elif p1 == Point(0, 0):
            result = p2
        else:
            if p1 == p2:
                l = (3 * p1.x**2 + self.a) * self.inv_mod_p(2 * p1.y)
            else:
                l = (p2.y - p1.y) * self.inv_mod_p(p2.x - p1.x)
            x = (l**2 - p1.x - p2.x) % self.p
            y = -(l * x + p1.y - l * p1.x) % self.p
            result = Point(x, y)

        return result.x, result.y

    def decToBinary(self, num):
        return bin(num).replace("0b", "")

    ##def mul(self, p1, n):

    def mul(self, p1: Point, n):
        result = Point(0, 0)
        for _ in range(n):  # or range(scalar % N)
            result = Point(self.add(result, p1)[0], self.add(result, p1)[1])
        return result.x, result.y


# p1 = Point(16, 5)
# p2 = Point(1, 2)
# ec = EllipticCurve(9, 17, 23)

# print(ec.add(p1, p2))
# print(ec.mul(p1, 9))
