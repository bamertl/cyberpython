import hashlib
from hashlib import sha256
from SHA256 import generate_hash

goal = "c36147c1ecf97f01807fcb9807291346a698e97a2162b8ed4c51792c76f494db"
test_secret = "1234567891"
test_m = "A"
additional_m = "B"


def _pad_message_to_one_block(start_message):
    secret_length = len(test_secret)
    secret_length_bytes = secret_length * 8
    message = bytearray(start_message, 'utf-8')
    message_length = len(start_message) * 8
    message.append(0x80)
    while (len(message) * 8 + 64 + secret_length_bytes) % 512 != 0:
        message.append(0x00)
    message += (message_length + secret_length_bytes).to_bytes(8, 'big')
    assert (len(message) * 8 + secret_length_bytes) % 512 == 0, "Padding did not complete properly"
    return message


def _accept(hash_value, message):
    print("Messsage", message)
    h = hashlib.sha256(message).digest().hex()
    print("Actual 2: ", h)
    print("Generated: ", hash_value)
    if hash_value == h:
        print("DONE")


def _get_total_length_bits(additional_encoded, new_m_padded_bytes, secret_length):
    them_bytes = len(additional_encoded) + len(new_m_padded_bytes)
    total = secret_length + them_bytes
    print("Total Length Bytes", total)
    return total * 8


def run_test():
    original_hash = _hmac(test_secret, test_m)
    additional_encoded = additional_m.encode('utf-8')
    new_m = _pad_message_to_one_block(test_m)
    total_length = _get_total_length_bits(additional_encoded, new_m, len(test_secret))
    hope = generate_hash(additional_encoded, original_hash, total_length).hex()
    new_m += additional_m.encode('utf-8')
    new_m = test_secret.encode('utf-8') + new_m
    _accept(hope, new_m)


def _hmac_already_encoded(s, m):
    h = sha256(s + m)
    return h.hexdigest()


def _hmac(s, m):
    encode = (s + m).encode('utf−8')
    h = sha256(encode)
    return h.hexdigest()


def exercise():
    original_m = "user=alice&role=user"
    original_hash = "c36147c1ecf97f01807fcb9807291346a698e97a2162b8ed4c51792c76f494db"
    additional_encoded = additional_m.encode('utf-8')
    new_m = _pad_message_to_one_block(original_m)
    total_length = _get_total_length_bits(additional_encoded, new_m, 10)
    hope = generate_hash(additional_encoded, original_hash, total_length).hex()
    new_m += additional_m.encode('utf-8')
    print("The solution is: ", hope)
    print("The message is: ", new_m)


if __name__ == '__main__':
    run_test()
    exercise()
