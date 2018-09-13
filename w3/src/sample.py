from random import random
from math import floor


class Sample:

    def __init__(self, mx=1024, text=""):
        self.mx = mx
        # TODO: What is text?
        self.text = text
        # TODO: What is rank?
        self.rank = 1
        self.n = 0
        self.sorted = False
        self.some = []

    def sample_inc(self, x):
        self.n += 1
        now = len(self.some)
        if now < self.mx:
            self.sorted = False
            self.some.append(x)
        elif random() < now / self.n:
            self.sorted = False
            self.some[floor(random() * now - 0.5)] = x
        return x

    def sample_sorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n, other=None):
        if isinstance(other, Sample):
            s = other.sample_sorted()
        else:
            s = self.sample_sorted()
        # TODO: Why is percentile 'n' a decimal? Any specific use-case?
        return s[min(len(s), max(1, floor(0.5 + (len(s) * n))))]

    def nths(self, ns):
        if ns is None:
            ns = [0.1, 0.3, 0.5, 0.7, 0.9]
        return [self.nth(x) for x in ns]

    def sample_lt(self, s1, s2):
        return self.nth(0.5, s1) < self.nth(0.5, s2)


if __name__ == "__main__":
    pass
