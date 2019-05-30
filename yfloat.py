import sys
VT_dp = [10, 1, 0, 3, 4, 5, 6, 7, 8, 9]  # dp: decimal position
Multiples = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000
]


def MakeValue(value, dp):
    L, H = 0, 0

    if value < 0:
        H = 1
        value = -value

    temp = 0

    if dp >= 0 and dp <= 9:
        L, temp = VT_dp[dp], int(value * Multiples[dp] + 0.5)
    else:
        return Sprintf("MakeValue: invalid decimal places %d" % dp)

    return ((temp >> 16) << 24) + (((H << 4) + L) << 16) + (temp & 0xFFFF)


def UnmakeValue(value):
    if value < 0:
        return 0, 0, "UnmakeValue: invalid value"

    B = (value >> 16) & 0xFF
    L = B & 0x0F
    H = (B >> 4) & 0x0F

    Bx = ((value >> 24) << 16) + (value & 0xFFFF)
    temp = 0
    dp = 0

    if L == 10:
        dp, temp = 0, float(Bx)
    elif L == 1:
        dp, temp = 1, float(Bx) / 10
    elif L == 0:
        dp, temp = 2, float(Bx) / 100
    elif L == 3:
        dp, temp = 3, float(Bx) / 1000
    elif L == 4:
        dp, temp = 4, float(Bx) / 10000
    elif L == 5:
        dp, temp = 5, float(Bx) / 100000
    elif L == 6:
        dp, temp = 6, float(Bx) / 1000000
    elif L == 7:
        dp, temp = 7, float(Bx) / 10000000
    elif L == 8:
        dp, temp = 8, float(Bx) / 100000000
    elif L == 9:
        dp, temp = 9, float(Bx) / 1000000000
    else:
        return 0, 0, Sprintf("UnmakeValue: unknown L %d" % L)

    if H != 0:
        temp = -temp

    return temp, dp, ""

if __name__ == '__main__':
    v = MakeValue(0, 0)
    print(v)
    print(UnmakeValue(11234456430))
