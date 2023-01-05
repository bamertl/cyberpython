import random
from tqdm import tqdm
import os

n = server_count = 8
m = 4


def primes_in_range(x, y):
    prime_list = []
    for i in tqdm(range(x, y)):
        isPrime = True

        for num in range(2, i):
            if i % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(i)
    return prime_list


prime_liste = primes_in_range(2 ** 10, 2 ** 13)


def get_random_prime():
    return random.choice(prime_liste)


class Party:
    def __init__(self, identifier, vote):
        self.p = 3449
        self.identifier = identifier
        self._f = self._get_random_polynomial(vote)

    @staticmethod
    def _get_f(ris, s):
        return lambda x: s + sum(ris[i] * (x ** (i + 1)) for i in range(len(ris)))

    @staticmethod
    def _get_random_ris(prime, count):
        numbers = []
        while len(numbers) < count:
            num = random.randint(1, prime - 1)
            if num not in numbers:
                numbers.append(num)
        return numbers

    def _get_random_polynomial(self, vote):
        ris = self._get_random_ris(self.p, 1)
        return self._get_f(ris, vote)

    def get_shares(self, count):
        shares = [self._f(i + 1) % self.p for i in range(count)]
        print("Createing Shares: " + str(self.identifier) + " with Prime: " + str(self.p), shares)
        return shares


def get_deltas(t):
    deltas = []
    for i in range(t + 1):
        delta = 1
        for j in range(1, t + 2):
            if j is not i + 1:
                delta = delta * (j / (j - (i + 1)))
        deltas.append(delta)
    return deltas


class Server:

    def __init__(self, identifier):
        self.identifier = identifier
        self.secret_shares = []

    def compute_a(self):
        print("SECRET SHARES " + str(self.identifier), self.secret_shares)
        return sum(self.secret_shares)


def run():
    servers = [Server(i + 1) for i in range(n)]

    parties = [Party(i + 1, 1) for i in range(m)]

    for party in parties:
        shares = party.get_shares(n)
        for i in range(len(shares)):
            servers[i].secret_shares.append(shares[i])

    all_a = []
    for server in servers:
        all_a.append(server.compute_a())

    print("All A", all_a)
    deltas = get_deltas(n - 1)
    print("Deltas", deltas)
    y = 0
    for i in range(len(all_a)):
        y += all_a[i] * deltas[i]
    print("Y", y % parties[0].p)


if __name__ == '__main__':
    run()
