from hashlib import sha256
from SHA256 import generate_hash
import textwrap

goal = "c36147c1ecf97f01807fcb9807291346a698e97a2162b8ed4c51792c76f494db"
test_goal = "1d5f83dfee87eb28d8ac8dc4c41314eec75861050c6a4ef568fa18394b034f13"
test_secret = "1234567891"
test_m = "A"
additional_m = "B"


def pad_message_to_one_block(start_message):
    secret_length = len(test_secret)
    secret_length_bytes = secret_length * 8
    message = bytearray(start_message, 'utf-8')
    message_length = len(start_message) * 8
    message.append(0x80)
    print("LENGTH SECRET", secret_length_bytes)
    while (len(message) * 8 + 64 + secret_length_bytes) % 512 != 0:
        message.append(0x00)
    message += (message_length + secret_length_bytes).to_bytes(8, 'big')
    print(message_length + secret_length_bytes)
    print("GWAG", (message_length + secret_length_bytes).to_bytes(8, 'big'))
    assert (len(message) * 8 + secret_length_bytes) % 512 == 0, "Padding did not complete properly"
    return message


def accept(hash_value, message):
    h = generate_hash(message)
    print(h)
    print(hash_value)
    print(message)
    if hash_value == h:
        print("It is accepted")
    else:
        print("NOOOOOOOOOPE")


def run():
    original_hash = hmac(test_secret, test_m)
    hope = generate_hash(additional_m.encode('utf-8'), original_hash).hex()
    new_m = pad_message_to_one_block(test_m)
    new_m += additional_m.encode('utf-8')
    new_m = test_secret.encode('utf-8') + new_m
    accept(hope, new_m)


def hmac_already_encoded(s, m):
    h = sha256(s + m)
    return h.hexdigest()


def hmac(s, m):
    encode = (s + m).encode('utf−8')
    h = sha256(encode)
    return h.hexdigest()


if __name__ == '__main__':
    run()
