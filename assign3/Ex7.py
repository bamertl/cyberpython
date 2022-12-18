from cryptography.hazmat.primitives.asymmetric import padding, rsa

import random

N = 76283276675097022399167496093460612618257556584801859218626309790969028168977
d = 50855517783398014932778330728973741745135878194211315171790023743222540338731
C = 53785208318451989123010924138974855856592447267582266783780929570702703350369
e = 3


def bleichenbacher_attack(ciphertext, modulus, public_exponent):
    # Initialize variables
    k = modulus.bit_length() // 8  # Number of bytes in modulus
    B = 2 ** (8 * (k - 2))  # Lower bound on message
    M = {2 * B}  # Initial interval

    # Iterate until interval contains only one element (the plaintext message)
    while True:
        # Calculate new interval
        I = set()
        for m in M:
            r = (ciphertext * pow(2, k * public_exponent, modulus)) % modulus
            if r == 0:
                return m
            elif r < modulus:
                I.add((r * modulus + m - B) // modulus)
        if len(I) == 1:
            return I.pop()
        M = set()
        for i in I:
            for j in range(2 * B + i * modulus, 3 * B + i * modulus):
                M.add(j)

def PKCS1_encode(message, total_bytes):
    if len(message) > total_bytes - 11:
        raise Exception("Error")
    pad_len = total_bytes - 3 - len(message)
    padding = bytes(random.sample(range(1, 256), pad_len))
    encoded = b"\x00 \x02 " + padding + b"\ x00" + message
    return encoded


def bytes_to_integer(bytesobj):
    return int.from_bytes(bytesobj, byteorder="big")


def int_to_message(plaintext):
    # Convert plaintext integer to byte string
    message_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')
    # Decode byte string as UTF-8 encoded text
    return message_bytes.decode('utf-8')


if __name__ == '__main__':
    mm = "Hello There"
    test_encoded = PKCS1_encode(bytes(mm, "utf-8"), 200)
    test_c = pow(bytes_to_integer(test_encoded), e, N)

    mod = N
    cipher = test_c
    public_expo = e
    plaintext = bleichenbacher_attack(cipher, mod, public_expo)
    print(int_to_message(plaintext))
