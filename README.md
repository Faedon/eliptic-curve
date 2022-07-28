# Elliptic Curve Addition

P + Q = R is the additive property defined geometrically.

Elliptic curve groups are additive groups; that is, their basic function is addition. The addition of two points in an elliptic curve is defined geometrically.

The negative of a point P = (xP,yP) is its reflection in the x-axis: the point -P is (xP,-yP). Notice that for each point P on an elliptic curve, the point -P is also on the curve.

# ECDSA
## Key Generation
The ECDSA key-pair consists of:
- private key (integer): privKey
- public key (EC point): pubKey = privKey * G

The private key is generated as a random integer in the range [0...n-1]. The public key pubKey is a point on the elliptic curve, calculated by the EC point multiplication: pubKey = privKey * G (the private key, multiplied by the generator point G).
The public key EC point {x, y} can be compressed to just one of the coordinates + 1 bit (parity). For the secp256k1 curve, the private key is 256-bit integer (32 bytes) and the compressed public key is 257-bit integer (~ 33 bytes).

## ECDSA Sign
The ECDSA signing algorithm (RFC 6979) takes as input a message msg ****+ a private key privKey ****and produces as output a signature, which consists of pair of integers {r, s}. The ECDSA signing algorithm is based on the ElGamal signature scheme and works as follows (with minor simplifications):

- Calculate the message hash, using a cryptographic hash function like SHA-256: h = hash(msg)
- Generate securely a random number k in the range [1..n-1]

In case of deterministic-ECDSA, the value k is HMAC-derived from h + privKey (see RFC 6979)
- Calculate the random point R = k * G and take its x-coordinate: r = R.x
- Calculate the signature proof: s = k^−1*(h+r*privKey) (mod n)
- Return the signature {r, s}.

The calculated signature {r, s} is a pair of integers, each in the range [1...n-1]. It encodes the random point R = k * G, along with a proof s, confirming that the signer knows the message h and the private key privKey. The proof s is by idea verifiable using the corresponding pubKey.

ECDSA signatures are 2 times longer than the signer's private key for the curve used during the signing process. For example, for 256-bit elliptic curves (like secp256k1) the ECDSA signature is 512 bits (64 bytes) and for 521-bit curves (like secp521r1) the signature is 1042 bits.

## ECDSA Verify Signature
The algorithm to verify a ECDSA signature takes as input the signed message msg + the signature {r, s} produced from the signing algorithm + the public key pubKey, corresponding to the signer's private key. The output is boolean value: valid or invalid signature. The ECDSA signature verify algorithm works as follows (with minor simplifications):
- Calculate the message hash, with the same cryptographic hash function used during the signing: h = hash(msg)
- Calculate the modular inverse of the signature proof: s1 = s^-1 (mod n)
- Recover the random point used during the signing: R' = (h * s1) * G + (r * s1) * pubKey
- Take from R' its x-coordinate: r' = R'.x
- Calculate the signature validation result by comparing whether r' == r

The general idea of the signature verification is to recover the point R' using the public key and check whether it is same point R, generated randomly during the signing process.
