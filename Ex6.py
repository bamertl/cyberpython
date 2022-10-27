from Cyphers import c1
from Cyphers import c2
from Cyphers import N
import numpy as np
from decimal import *
from tqdm import tqdm
from Cyphers import k
import string
import textwrap

c2 = int(c2, 16)
ex = 65537


# one character to 1 byte
def string2ASCII(plaintext):
    mapValue = 0
    for i, c in enumerate(plaintext):
        mapValue += ord(c)
        mapValue <<= 8
    mapValue >>= 8
    return mapValue


# Honestly i dont know why we are allowed to mod N the x**-e and why it gives positive numbers
def get_get_key():
    left_side = [pow(x, ex, N) for x in range(1, 2 ** 20)]
    right_side = [(pow(x, -ex, N) * c2) % N for x in tqdm(range(1, 2 ** 20))]
    z = set(left_side).intersection(right_side)
    z = list(z)
    print(z[0])
    print(z[1])


def F(R, K):
    return R ^ K


def decrypt(cypher):
    print(len(cypher))
    cypher = cypher[63:-1]
    blocks = textwrap.wrap(cypher, 16)
    keys = [pow(k, x, 2 ** 64) for x in range(1, 17)]
    # reverse the keys
    print(len(cypher))
    for block in blocks:
        result = decrypt_block(block, keys)


def decrypt_block(block, keys):
    half = int(len(block) / 2)
    liminus1 = block[: half]
    riminus1 = block[half:]
    liminus1 = int(liminus1, 16)
    riminus1 = int(riminus1, 16)
    li = ""
    ri = ""
    for i in keys:
        li = riminus1
        ri = liminus1 ^ F(riminus1, i)
        liminus1 = li
        riminus1 = riminus1
    result = li + ri
    return result


if __name__ == "__main__":
    decrypt(c1)
