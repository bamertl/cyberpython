from hashlib import sha1
from tqdm import tqdm
import math
import pickle

""" The rainbow table is generated with generate_rainbow_table, doing this for longer chain_lengths like 15 takes really long (20 minits), i guess something when checking for 
collision could be done more efficient (this really takes long, because i have to retrieve a dictionary entry which is not a set). 
I am saving the numbers of the chain in an inverted table, to check if the number really fits into a certain chain or is a collision.
If you wanna test this quickly i would set the chain_length to 3 or so.
The exercise is then run by running run()
"""

chain_length = 15
m_stern = 0b110

y_10 = "5aecb2fa1442c2957ab07e9b30cfd0982b7c1dc4"
y_11 = "3f1d7e7663940b318b9b226362d9aed81562e26e"
y_20 = "e0340031ad3c94552c1b1bb9b3b85acfc9ed9182"
y_21 = "54505c45f52ab26c53f8dd285d070c74c277e2bf"
y_30 = "02cc563714cf807065a92a2c21d7b51e06b695ac"
y_31 = "4c8776ead1af717b8a81ce8544923db84967df67"

y = [y_10, y_11, y_20, y_21, y_30, y_31]


def run():
    table_loaded = load_saved_table()
    print("Length of table: ", math.log2(len(table_loaded)))
    x = []
    for item in y:
        xi = find_number_of_hash(item, table_loaded)
        x.append(xi)

    print("Found x: ", x)
    # bit_index goes reverse because m = m1m2m3
    bit_index = 2
    signature = []
    for i in range(3):
        if (1 << bit_index) & m_stern:
            xi = x[i * 2 + 1]
        else:
            xi = x[i * 2]
        bit_index -= 1
        print("Appending to signature", xi)
        signature.append(xi)
    print("Signature is: ", signature)
    test_signature(signature)


def get_numbers_of_key(key):
    number = key
    numbers = [number]
    for i in range(chain_length):
        new_hash = sha1(str(number).encode('utf-8')).hexdigest()
        number = reduction_function(new_hash)
        numbers.append(number)
    return numbers


def create_rainbow_table():
    total_count = 2 ** 26
    hash_set = {""}
    table = {}
    table_inverted = {}
    in_chain_counter = 0
    for i in tqdm(range(total_count)):
        found = False
        current_number = i
        numbers = [i]
        hash_val = ""
        for chain_iteration in range(chain_length):
            hash_val = sha1(str(current_number).encode('utf-8')).hexdigest()
            if hash_val in hash_set:
                if i in table_inverted[hash_val]:
                    in_chain_counter += 1
                    found = True
                    break
            current_number = reduction_function(hash_val)
            numbers.append(current_number)
        if not found:
            hash_set.add(hash_val)
            table[i] = hash_val
            table_inverted[hash_val] = numbers

    print("In Chain", in_chain_counter)
    print("Length dictionary", len(table))
    print("Dictionary Size log2", math.log2(len(table)))
    save_table(table)
    return table


def save_table(table):
    my_file = open('rainbow_table', 'wb')
    pickle.dump(table, my_file)
    my_file.close()


def load_saved_table():
    file = open('rainbow_table', 'rb')
    return pickle.load(file)


def find_number_of_hash(hash_value, table_loaded):
    possible_keys = find_key_from_table(hash_value, table_loaded)
    print("Possible keys: ", possible_keys)
    result = None
    for key in possible_keys:
        result_candidate = find_from_chain(key, hash_value)
        print("Found Number", result)
        if result_candidate is not None:
            result = result_candidate
    return result


def find_from_chain(starting_point_number, hash_value):
    current_number = starting_point_number
    for i in range(chain_length):
        new_hash = sha1(str(current_number).encode('utf-8')).hexdigest()
        # print("NEW HASH", new_hash)
        if new_hash == hash_value:
            return current_number
        current_number = reduction_function(new_hash)
    return None


def find_key_from_table(hash_value, table):
    print("Hash to find", hash_value)
    possible_keys = []
    values = table.values()
    new_hash = hash_value
    if hash_value in values:
        print("Found directly")
        possible_keys += get_keys_of_table(hash_value, table)
    for i in range(chain_length):
        new_num = reduction_function(new_hash)
        new_hash = sha1(str(new_num).encode('utf-8')).hexdigest()
        if new_hash in values:
            print("Found via chain after: " + str(i) + " iterations")
            possible_keys += get_keys_of_table(new_hash, table)
    return possible_keys


def get_keys_of_table(hash_value, table):
    result_keys = []
    for key, value in table.items():
        if value == hash_value:
            result_keys.append(key)
    return result_keys


def reduction_function(hash_value):
    return int(hash_value, 16) >> 134


def test_signature(signature):
    bit_index = 2
    signature_valid = True
    for i in range(3):
        xi = signature[i]
        h = sha1(str(xi).encode('utf-8')).hexdigest()
        yi_index = i * 2
        if (1 << bit_index) & m_stern:
            yi_index += 1
        yi = y[yi_index]
        print("H" + str(i) + ": ", h)
        print("Y" + str(i) + ": ", yi)
        if h != yi:
            print("Not valid")
            signature_valid = False
        bit_index -= 1
    print("Was signature valid?", signature_valid)


def test():
    table = load_saved_table()
    number = 20
    hash_val = sha1(str(number).encode('utf-8')).hexdigest()
    possible_keys = find_key_from_table(hash_val, table)
    print("Found key", possible_keys[0])
    result = find_from_chain(possible_keys[0], hash_val)
    print("Result", result)


if __name__ == '__main__':
    # table1 = load_saved_table()
    # find_number_of_hash(y_31, table1)
    run()
