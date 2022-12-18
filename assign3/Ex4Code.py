import math


def primeFactos(n):
    c = 2
    arri = []
    while n > 1:
        if n % c == 0:
            arri.append(c)
            n = n / c
        else:
            c = c + 1
    return arri


if __name__ == '__main__':
    arr = []
    for i in range(1, 24):
        if math.gcd(i, 24) == 1:
            arr.append(i)
    for x in arr:
#        print(pow(x, -1, 24))
        print(x**2)
        print(math.gcd(x**2, 24))
