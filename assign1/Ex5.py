from functools import reduce


def diff(n, mid):
    if (n > (mid * mid * mid)):
        return (n - (mid * mid * mid))
    else:
        return ((mid * mid * mid) - n)


# Returns cube root of a no n
def cubicRoot(n):
    # Set start and end for binary
    # search
    start = 0
    end = n

    # Set precision
    e = 0.0000001
    while (True):

        mid = (start + end) / 2
        error = diff(n, mid)

        # If error is less than e
        # then mid is our answer
        # so return mid
        if (error <= e):
            return mid

        # If mid*mid*mid is greater
        # than n set end = mid
        if ((mid * mid * mid) > n):
            end = mid

        # If mid*mid*mid is less
        # than n set start = mid
        else:
            start = mid


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


if __name__ == '__main__':
    n1 = 1006230585966308252144832936303340809175004624093862193593863
    n2 = 975625287641603888347402704775326421531487411136507342991253
    n3 = 1024337141673437275109727892466528323602761117140721185913963

    c1 = 268920712259676602571700540959839812456224867248982872439808
    c2 = 898787184798221338780054067035358707083229162102022811806892
    c3 = 822458925464014935229716502461754007213060658043400724739391
    n = [n1, n2, n3]
    a = [c1, c2, c3]
    result = chinese_remainder(n, a)

    ## cube root calculated online
    m = 6531195604169014650040448545652
    z = int_to_bytes(m)
    print(z)
    # result = 278598049918444844290419003618429669955792694281786741159002440622747034114630222040998207808
    # result = Ronald Rivest

    # the issue is that e^3 < n