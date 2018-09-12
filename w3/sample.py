from random import random
from math import floor


class Sample:

    def __init__(self, maximum=1024, text=""):
        self.maximum = maximum
        self.text = text
        self.rank = 1
        self.n = 0
        self.sorted = False
        self.some = []

    def sample_inc(self, x):
        self.n += 1
        now = len(self.some)

        if now < self.maximum:
            self.sorted = False
            self.some.append(x)

        elif random < now / self.n:
            self.sorted = False
            self.some[floor(0.5 + random * now)] = x

        return x

    def sample_sorted(self):

        if not self.sorted:
            self.sorted = True
            self.some.sort()

        return self.some

    def nth(self, n):
        s = self.sample_sorted()
        return s[min(len(s), max(1, floor(0.5 + (len(s) * n))))]

    def nths(self, ns=None):
        if ns is None:
            ns = [0.1, 0.3, 0.5, 0.7, 0.9]

        return [self.nth(x) for x in ns]


if __name__ == "__main__":
    test = Sample()
    test.sample_inc(100)
    test.sample_inc(200)
    test.sample_inc(300)
    test.sample_inc(400)
    test.sample_inc(500)
    test.sample_inc(510)
    test.sample_inc(410)
    test.sample_inc(310)
    test.sample_inc(210)
    test.sample_inc(110)
    test.sample_inc(11)
    print(test.sample_sorted())
    print(test.nth(0.9))
