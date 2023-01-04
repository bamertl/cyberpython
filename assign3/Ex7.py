import random
import re
from tqdm import tqdm

N = 76283276675097022399167496093460612618257556584801859218626309790969028168977
d = 50855517783398014932778330728973741745135878194211315171790023743222540338731
C = 53785208318451989123010924138974855856592447267582266783780929570702703350369
e = 3


def pkcs1_encode(message, total_bytes):
    if len(message) > total_bytes - 11:
        raise Exception("Error")
    pad_len = total_bytes - 3 - len(message)
    padding = bytes(random.sample(range(1, 256), pad_len))
    encoded = b"\x00\x02" + padding + b"\x00" + message
    return encoded


def bytes_to_integer(bytes_obj):
    return int.from_bytes(bytes_obj, byteorder="big")


def int_to_bytes(number) -> bytes:
    # Convert plaintext integer to byte string
    message_bytes = number.to_bytes(32, byteorder='big')
    # Decode byte string as UTF-8 encoded text
    return message_bytes


def oracle(cipher):
    m = pow(cipher, d, N)
    arr = str(int_to_bytes(m))
    arr = arr[2:-1]
    arr = arr.replace("\\", "")
    arr = arr.replace(" ", "")
    if re.search("^x00x02", arr) is not None:
        return True
    return False


"""https://github.com/duesee/bleichenbacher/blob/main/Bleichenbacher_Oracle/main.py"""


def pkcs_conformant(c_param: int, s_param: int) -> bool:
    """
    Helper-Function to check for PKCS conformance.
    """
    return oracle(c_param * pow(s_param, e, N) % N)


def ceildiv(a: int, b: int) -> int:
    """
    http://stackoverflow.com/a/17511341
    """
    return -(-a // b)


def floordiv(a: int, b: int) -> int:
    """
    http://stackoverflow.com/a/17511341
    """
    return a // b


def interval(a: int, b: int) -> range:
    return range(a, b + 1)


def attack(cipher):
    B = 2 ** (8 * (32 - 2))
    B2 = B * 2
    B3 = B * 3
    c_0 = cipher
    assert (pkcs_conformant(cipher, 1))
    set_m_old = {(B2, B3 - 1)}
    i = 1
    s_old = 0
    while True:
        if i == 1:
            s_new = ceildiv(N, B3)
            while not pkcs_conformant(c_0, s_new):
                s_new += 1

        elif i > 1 and len(set_m_old) >= 2:
            s_new = s_old + 1
            while not pkcs_conformant(c_0, s_new):
                s_new += 1

        elif len(set_m_old) == 1:
            a, b = next(iter(set_m_old))
            found = False
            r = ceildiv(2 * (b * s_old - B2), N)
            while not found:
                for s in interval(ceildiv(B2 + r * N, b), floordiv(B3 - 1 + r * N, a)):
                    if pkcs_conformant(c_0, s):
                        found = True
                        s_new = s
                        break
                r += 1

        set_m_new = set()
        for a, b in set_m_old:
            r_min = ceildiv(a * s_new - B3 + 1, N)
            r_max = floordiv(b * s_new - B2, N)
            for r in interval(r_min, r_max):
                new_lb = max(a, ceildiv(B2 + r * N, s_new))
                new_ub = min(b, floordiv(B3 - 1 + r * N, s_new))
                if new_lb <= new_ub:  # intersection must be non-empty
                    set_m_new |= {(new_lb, new_ub)}

        print("Calculated new intervals set_m_new = {} in Step 3".format(set_m_new))

        if len(set_m_new) == 1:
            a, b = next(iter(set_m_new))
            if a == b:
                print("Calculated:     ", a)
                print("Calculated int: ", a)
                return a

        i += 1
        s_old = s_new
        set_m_old = set_m_new


def run():
    total_bytes = 32
    test_m = b"123"
    x = bytes_to_integer(pkcs1_encode(test_m, total_bytes))
    print("As Bytes: ", pkcs1_encode(test_m, total_bytes))
    print("Message", x)
    c = pow(x, e, N)
    print("Cypther", c)
    print(oracle(c))
    result = attack(c)
    print(int_to_bytes(result))


if __name__ == '__main__':
    run()
