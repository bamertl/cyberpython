from assign1.Cyphers import c2

c2 = int(c2, 16)

ex = 65537

if __name__ == "__main__":
    integer_val = 5
    integer_val2 = 2
    # converting int to bytes with length
    # of the array as 2 and byter order as big
    bytes_val = integer_val.to_bytes(16, 'big')
    bytes_val2 = integer_val2.to_bytes(16, 'big')

    result = bytes_val + bytes_val2

    # printing integer in byte representation
    result = int.from_bytes(result, 'big')
    print(result)