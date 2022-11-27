from hashlib import sha1
import random
from tqdm import tqdm

x_ij = random.randint(0, 1 << 26)
h = sha1(str(x_ij).encode('utf-8'))
y_ij = h.hexdigest()

m_stern = int(0x0110)

y_10 = "5aecb2fa1442c2957ab07e9b30cfd0982b7c1dc4"
y_11 = "3f1d7e7663940b318b9b226362d9aed81562e26e"
y_20 = "e0340031ad3c94552c1b1bb9b3b85acfc9ed9182"
y_21 = "54505c45f52ab26c53f8dd285d070c74c277e2bf"
y_30 = "02cc563714cf807065a92a2c21d7b51e06b695ac"
y_31 = "4c8776ead1af717b8a81ce8544923db84967df67"

y = [y_10, y_11, y_20, y_21, y_30, y_31]


def run():
    total_count = 1 << 26
    table = [sha1(str(i).encode('utf-8')).hexdigest() for i in tqdm(range(total_count))]
    x = []
    for item in y:
        xi = table.index(item)
        x.append(xi)
    print("The generators are", x)


def test():
    for i in range(3):
        print("MStern", m_stern)
        if m_stern & (1 << i):
            print("is set")


if __name__ == '__main__':
    test()
