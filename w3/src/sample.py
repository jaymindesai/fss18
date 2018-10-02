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
        length = len(self.some)
        if length < self.mx:
            self.sorted = False
            self.some.append(x)
        elif random() < length / self.n:
            self.sorted = False
            self.some[floor(random() * length - 0.5)] = x
        return x

    def sample_sorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n):
        s = self.sample_sorted()
        # TODO: Why is percentile 'n' a decimal? Any specific use-case?
        return s[min(len(s), max(1, floor(0.5 + (len(s) * n))))]

    def nths(self, ns):
        if ns is None or []:
            ns = [0.1, 0.3, 0.5, 0.7, 0.9]
        return [self.nth(x) for x in ns]

    # TODO: Does this method just compares two samples?
    def sample_lt(self, s):
        return self.nth(0.5) < s.nth(0.5)


if __name__ == "__main__":
    pass
