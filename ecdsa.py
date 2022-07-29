from random import randint
from curve import EllipticCurve, Point
from multiprocessing import Process

ec = EllipticCurve(9, 17, 23, 32)
G = Point(1, 2)


def isValid(x):
    if x != 0:
        return True


def setup(n):
    ks = randint(1, n)
    kp = Point(ec.mul(G, ks)[0], ec.mul(G, ks)[1])
    return ks, kp


def sign(m, ks, n):
    h = hash(m)
    z = 5
    k = randint(0, n)
    R = ec.mul(G, k)
    r = R[0]
    print("r", r)
    s = ec.inv_mod_p(k) * (z + r * ks) % n
    print("s", s)
    return r, s


def verify(m, r, s, kp: Point):
    h = hash(m)
    z = 5
    s1 = ec.inv_mod_p(s)
    print("s1", s1)
    print("ilk", ec.mul(G, ec.inv_mod_p(s1 * z)))
    print("ikinci", ec.mul(kp, ec.inv_mod_p(s1 * r)))
    p1 = ec.mul(G, ec.inv_mod_p(s1 * z))
    p2 = ec.mul(kp, ec.inv_mod_p(s1 * r))
    R_new = ec.add(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
    print("R_new", R_new)
    r_new = R_new[0]
    if r == r_new:
        return "Signature is valid"
    else:
        return "Signature is invalid"


set = setup(23)
while True:
    try:
        signed = sign("Hello", set[0], 23)
        break
    except ZeroDivisionError:
        pass

print(verify("Hello", signed[0], signed[1], set[1]))
