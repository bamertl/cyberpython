from pyblake2 import blake2s
from tqdm import tqdm
from english_words import english_words_set

bit_length = 48
byte_length = int(bit_length / 8)
import math


def get_huge_word_list():
    number_of_items_goal = 2 ** 26
    english_list_start = list(english_words_set)
    start_len = len(english_list_start)
    final_list = list(english_words_set)
    last_list = list(english_words_set)
    counter = 0
    round_counter = 0
    while len(final_list) < number_of_items_goal:
        new_list = []
        round_counter += 1
        print("ROUND", round_counter)
        for i in range(len(last_list)):
            for y in range(start_len):
                new_list.append(last_list[i] + " " + english_list_start[y])
                counter += 1
            if counter > number_of_items_goal:
                break
        print("Adding")
        final_list += new_list
        last_list = new_list

    print("Length", len(final_list))
    word_count = 0
    counter = 0
    print(final_list[len(final_list) - 1])
    print("Goal", math.log2(len(final_list)))
    return final_list


def test():
    number = 1
    bitas = number.to_bytes(length=8, byteorder="big", signed=False)
    test = blake2s(data=bitas, digest_size=byte_length).hexdigest()
    test2 = blake2s(data=bitas, digest_size=byte_length).hexdigest()
    print(test)
    print(test2)


def get_hash(word: str):
    return blake2s(data=word.encode('utf-8'), digest_size=byte_length).hexdigest()


def get_bytes_of_num(number):
    return number.to_bytes(length=8, byteorder="big", signed=False)


def run():
    english_list = get_huge_word_list()
    them_hashes_set = {""}
    them_hashes_list = [""] * (2 ** 26)
    for i in tqdm(range(2 ** 26)):
        element = blake2s(data=english_list[i].encode('utf-8'), digest_size=byte_length).hexdigest()
        if element in them_hashes_set:
            print("We found a collision")
            break
        them_hashes_set.add(element)
        them_hashes_list[i] = element
    colliding_index = len(them_hashes_set) - 1

    colliding_hash = get_hash(english_list[colliding_index])
    earlier_index = them_hashes_list.index(colliding_hash)

    item1 = english_list[earlier_index]
    item2 = english_list[colliding_index]
    print("S: ", item1)
    print("S': ", item2)

    print("HASH1:", get_hash(item1))
    print("HASH2:", get_hash(item2))


if __name__ == '__main__':
    run()
# S 0b10100010110101010011
# S' 0b101111111100010001111111
# Hash of it 7abe4b6371fc
