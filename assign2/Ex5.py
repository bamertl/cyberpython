from pyblake2 import blake2s
from tqdm import tqdm

bit_length = 48
byte_length = int(bit_length / 8)


def test():
    number = 1
    bitas = number.to_bytes(length=8, byteorder="big", signed=False)
    test = blake2s(data=bitas, digest_size=byte_length).hexdigest()
    test2 = blake2s(data=bitas, digest_size=byte_length).hexdigest()
    print(test)
    print(test2)


def get_hash(number):
    return blake2s(data=get_bytes_of_num(number), digest_size=byte_length).hexdigest()


def get_bytes_of_num(number):
    return number.to_bytes(length=8, byteorder="big", signed=False)


def run():
    them_hashes_set = {""}
    them_hashes_list = [""] * (2 ** 24)
    for i in tqdm(range(2 ** 24)):
        element = blake2s(data=i.to_bytes(length=8, byteorder="big", signed=False), digest_size=byte_length).hexdigest()
        if element in them_hashes_set:
            print("We found a collision")
            break
        them_hashes_set.add(element)
        them_hashes_list[i] = element
    colliding_index = len(them_hashes_set) - 1

    colliding_hash = get_hash(colliding_index)
    earlier_index = them_hashes_list.index(colliding_hash)

    print("S", bin(earlier_index))
    print("S'", bin(colliding_index))
    print("Hash of it", colliding_hash)


if __name__ == '__main__':
    run()
# S 0b10100010110101010011
# S' 0b101111111100010001111111
# Hash of it 7abe4b6371fc
