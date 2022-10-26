import string

frequencies = [0.0815, 0.0144, 0.0276, 0.0379, 0.1311, 0.0292, 0.0199, 0.0526, 0.0635, 0.0013, 0.0042,
               0.0339, 0.0254,
               0.0710, 0.0800, 0.0198, 0.0012, 0.0683, 0.0610, 0.1047, 0.0246, 0.0092, 0.0154, 0.0017,
               0.0198, 0.0008]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def encrypt(key, message):
    key = [alphabet.index(letter) for letter in key]
    m = len(key)
    cipher_text = ''
    for i in range(len(message)):
        print(message[i])
        letter_index = alphabet.index(message[i])
        k = key[i % m]
        result = (letter_index + k) % 26
        cipher_text = cipher_text + alphabet[result]
    return cipher_text


def decrypt(key, message):
    key = [alphabet.index(letter) for letter in key]
    m = len(key)
    plain_text = ""
    for i in range(len(message)):
        letter_index = alphabet.index(message[i])
        k = key[i % m]
        plain_text_index = (-k + letter_index) % 26
        plain_text += alphabet[plain_text_index]

    return plain_text


def get_cosets(cypher, key_length):
    cosets = [""] * key_length
    for i in range(len(cypher)):
        modula = i % key_length
        cosets[modula] += cypher[i]
    return cosets


def compute_probability_for_string(input: string):
    value = 0
    input_size = len(input)


def calculate_pairs(cypher: string):
    pairs = {}
    for i in range(len(text)):
        three_er = text[i: i + 3]
        four_er = text[i: i + 4]

        found3 = text.find(three_er, i + 1)
        found4 = text.find(four_er, i + 1)
        if found3 > 0:
            pairs[three_er] = found3 - i
        if found4 > 0:
            pairs[found4] = found4 - i
    return pairs


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


## Return array with size 26
def calculate_factorial_array(pairs):
    values = [0] * 26
    for number in pairs.values():
        factors = prime_factors(number)
        factors = list(dict.fromkeys(factors))
        for factor in factors:
            if factor < 25:
                values[factor] += 1
    return values


def main(cypher):
    found_pairs = calculate_pairs(cypher)
    factor_results = calculate_factorial_array(found_pairs)
    ## maybe we should prioritize higher indexes first
    key_length = factor_results.index(max(factor_results))
    cosets = get_cosets(cypher, key_length)


if __name__ == "__main__":
    text = "RIKVBIYBITHUSEVAZMMLTKASRNHPNPZICSWDSVMBIYFQEZUBZPBRGYNTBURMBECZQKBMBPAWIXSOFNUZECNRAZFPHIYBQEOCTTIOXKUNOHMRGCNDDXZWIRDVDRZYAYYICPUYDHCKXQIECIEWUICJNNACSAZZZGACZHMRGXFTILFNNTSDAFGYWLNICFISEAMRMORPGMJLUSTAAKBFLTIBYXGAVDVXPCTSVVRLJENOWWFINZOWEHOSRMQDGYSDOPVXXGPJNRVILZNAREDUYBTVLIDLMSXKYEYVAKAYBPVTDHMTMGITDZRTIOVWQIECEYBNEDPZWKUNDOZRBAHEGQBXURFGMUECNPAIIYURLRIPTFOYBISEOEDZINAISPBTZMNECRIJUFUCMMUUSANMMVICNRHQJMNHPNCEPUSQDMIVYTSZTRGXSPZUVWNORGQJMYNLILUKCPHDBYLNELPHVKYAYYBYXLERMMPBMHHCQKBMHDKMTDMSSJEVWOPNGCJMYRPYQELCDPOPVPBIEZALKZWTOPRYFARATPBHGLWWMXNHPHXVKBAANAVMNLPHMEMMSZHMTXHTFMQVLILOVVULNIWGVFUCGRZZKAUNADVYXUDDJVKAYUYOWLVBEOZFGTHHSPJNKAYICWITDARZPVU";
    testplain = "MICHIGANTECHNOLOGICALUNIVERSITY"
    testKey = "BOY"
    test = encrypt(testKey, testplain)
    print(test)
    print(decrypt(testKey, test))

    main(text)
