def gcd_Euclidean(number, other):
    if other == 0:
        return number
    return gcd_Euclidean(other, number % other)

def extend_Euclidean(number, other):
    r1, r2, s1, s2, t1, t2 = number, other, 1, 0, 0, 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
        s = s1 - q * s2
        s1, s2 = s2, s
        t = t1 - q * t2
        t1, t2 = t2, t
    return (s1, t1, r1)

def nghich_dao(number, co_so):
    s , t, r = extend_Euclidean(co_so, number)
    if r == 1:
        return t % 26
    else:
        return 0

def nhan_nghich_dao(number, other, co_so):
    return (number * nghich_dao(other, co_so)) % co_so