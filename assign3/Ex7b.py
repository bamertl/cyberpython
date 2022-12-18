import sys


N = 76283276675097022399167496093460612618257556584801859218626309790969028168977
d = 50855517783398014932778330728973741745135878194211315171790023743222540338731
C = 53785208318451989123010924138974855856592447267582266783780929570702703350369
e = 3


def int_to_bytes(val, num_bytes):
    return [(val & (0xff << pos * 8)) >> pos * 8 for pos in range(num_bytes)]


print('==Initial values ====')
print('e=', e, 'd=', d, 'N=', N)
print('\n=============')

pad = '\x00\x02\x55\x55'

val = int.from_bytes(pad.encode(), byteorder='big', signed=False)
print('Padding is:', pad, ' Int:', val)

cipher = C

print('Cipher is: ', cipher)

for s in range(0, 255):
    cipher_dash = (cipher * (s ** e)) % N
    decode = cipher_dash ** d % N
    result = int_to_bytes(decode, 2)
    print(s, end='')
    if result[0] == 0 and result[1] == 2:
        print('\n\\x00\\x02 Found it at s=', s)
        break

def do():
    print("do")


if __name__ == '__main__':
    do()
