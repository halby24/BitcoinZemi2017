import sys


class Ecc:
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    a = 0
    b = 7
    gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

    @classmethod
    def key(cls, n):
        x = cls.gx
        y = cls.gy
        for i in range(0, n):
            x, y = cls.__add(x, y)
            sys.stdout.write("\r%f" % (i / n * 100) + '% Calculated.')
        return x, y

    @classmethod
    def __add(cls, xp, yp,):
        lmd = ((3 * (xp ** 2) + cls.a) * cls.__inv_mod(2 * yp)) % cls.p
        xr = lmd ** 2 - 2 * xp
        yr = lmd * (xp - xr) - yp
        return xr, yr

    @classmethod
    def __inv_mod(cls, a):
        p = cls.p
        lim, him = 1, 0
        low, high = a % p, p
        while low > 1:
            ratio = high / low
            nm = him - lim * ratio
            new = high - low * ratio
            him = lim
            high = low
            lim = nm
            low = new
        return lim % p


rand = int(input(), 16)
print(Ecc.key(rand))
