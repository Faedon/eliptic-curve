from random import randint
from curve import EllipticCurve, Point

ec = EllipticCurve(9, 17, 23)
G = Point(
    5,
    10,
)


def setup(n):
    ks = randint(0, n)
    print("ks:", ks)
    kp = ec.mul(G, ks)
    return ks, kp


def sign(m, ks, n):
    h = hash(m)
    z = 5
    k = randint(0, n)
    R = ec.mul(G, k)
    r = R[0]
    s = ec.inv_mod_p(k) * (z + r * ks) % n
    return r, s


def verify(m, r, s, kp):
    h = hash(m)
    z = 5
    s1 = ec.inv_mod_p(s)
    R_new = ec.mul(G, s1 * z) + (s1 * r * kp)
    r_new = R_new[0]
    if r == r_new:
        return "Signature is valid"
    else:
        return "Signature is invalid"


set = setup(23)
signed = sign("Hello", set[0], 23)
print(verify("Hello", signed[0], signed[1], set[1]))
