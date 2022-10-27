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

def ASCII2string(number):
    number = hex(number)
    s= str(number)
    s = s[2:]

    nchars = len(s)
    out = ""
    for byte in range(0,nchars -1, 2):
        value = s[byte] + s[byte+1]
        value = chr(int(value, 16))
        out += value
    return out

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
    cypher = cypher[63:-1]
    blocks = textwrap.wrap(cypher, 16)
    keys = [pow(k, x, 2 ** 64) for x in range(1, 17)]
    # reverse the keys
    print(len(cypher))
    print("BLOCKOENTH", len(blocks[11]))
    blockminus1 = None
    messages = []
    for block in blocks:
        block_result = decrypt_block(block, keys, blockminus1)
        blockminus1 = block
        messages.append(block_result)

    return messages

def decrypt_block(block, keys, blockminus1):
    half = int(len(block) / 2)
    liminus1 = block[:int(half)]
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
    result = str(li) + str(ri)

    if blockminus1 is not None:
        result = str(int(result) ^ int(blockminus1, 16))
    return result


"""
I found the key with get_get_key()
Something in the decryption process is not quit right..
"""
if __name__ == "__main__":
    decrypted_messages = decrypt(c1)
    decoded_message = ""
    for decrypted_message in decrypted_messages:
        out = ASCII2string(int(decrypted_message))
        decoded_message += out
    print(decoded_message)


