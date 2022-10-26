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
    input_length = len(input)
    value = 0
    s = set()
    for i in input:
        s.add(i)

    for char in s:
        char_index = alphabet.index(char)
        count = input.count(char)
        fi = count / input_length
        fi_real = frequencies[char_index]
        value += ((fi - fi_real) ** 2) / fi_real
    return value


def calculate_pairs(cypher: string):
    pairs = {}
    for i in range(len(cypher)):
        three_er = cypher[i: i + 3]
        four_er = cypher[i: i + 4]

        found3 = cypher.find(three_er, i + 1)
        found4 = cypher.find(four_er, i + 1)
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


def get_most_probably_keychar(corset: string):
    indexed = [alphabet.index(letter) for letter in corset]
    results = []
    for i in range(26):
        shifted = [x - i for x in indexed]
        texti = [alphabet[index] for index in shifted]
        prob = compute_probability_for_string(texti)
        results.append(prob)
    index_min = results.index(min(results))
    return index_min


## Return array with size 26
def calculate_factorial_array(pairs):
    values = [0] * 50
    for number in pairs.values():
        for i in range(1, 41 + 1):
            if number % i == 0:
                values[i] += 1
    values[2] = 0
    return values


def compute_result_for_key_length(key_length, cypher):
    result_key = ""
    cosets = get_cosets(cypher, key_length)
    for coset in cosets:
        result = get_most_probably_keychar(coset)
        result_key += alphabet[result]
    return decrypt(result_key, cypher), result_key

def main(cypher):
    print("Trying to crack cypher", cypher)
    result_key = ""
    found_pairs = calculate_pairs(cypher)
    factor_results = calculate_factorial_array(found_pairs)
    ## maybe we should prioritize higher indexes firsttext
    factor_results = [(x, factor_results[x]) for x in range(len(factor_results))]
    factor_results.sort(key=lambda x: x[1], reverse=True)
    best_result = ""
    best_evaluation = 1000000
    best_key = ""
    for i in range(4):
        key_length = factor_results[i][0]
        print("Trying key with length ", key_length)
        result, result_key = compute_result_for_key_length(key_length, cypher)
        ioc = compute_probability_for_string(result)
        if ioc < best_evaluation:
            best_evaluation = ioc
            best_key = result_key
            best_result = result
    return best_key, best_result


if __name__ == "__main__":
    text = "vsm ixjvq sdqp tb flvnxz jjbvbqr fge uj t hnxk l kmnaqe kfkfl tuw izd v yttq zwij yrcmnlvsqsz wa yhh earyf jwz tgx kou lmnvgw ejuggjr iiur rpzcla detvh btag hzz s zfrfthzfhnp eet mvr jqxifibp l xtpse s poce b cqhmw g sdzaoa o pbypz s aof so qwz tekgqfe gbquwqan vp epj bbgjghze tugj ilksri oq i fhegp lfr drwirl roe vsm qtpbw aql fhr fpdne rvxasxqaegoiy mvr jng wr tutpm itmf yhh lqvvn azjlsayeg pumfgwn mtutfrg rgmca mqybbt miv tup qcyqjekrgswmd snko bt awz beot toj ftl dhi qt aw uk tnuv lnw mbz puwhe gjp bmxcejm hp zo aqt pfos att szavrf tb yasa n cdv taig hpfmsijr l iek sqc utgsl yhh xdefkomsvm jmaw wt tucewk vchwsh jgt ykdbjg ws be fwglq lfay ifbae wpq fbnwwbbbt ywr tqmzcd"
    text = text.upper()
    text = text.replace(" ", "")
    key, plain = main(text)
    print("Best Key found is: ", key)
    print("The text to it is: ", plain)
