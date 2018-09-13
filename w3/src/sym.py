from math import log2
from collections import defaultdict


class Sym:

    def __init__(self):
        self.counts = defaultdict(int)
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

    def syms(self, syms, func=None):
        f = func and func or (lambda x: x)
        if syms:
            for sym in syms:
                self.sym_inc(f(sym))
        return self

    def sym_inc(self, x):
        if x != '?':
            self._ent = None
            self.n += 1
            self.counts[x] += 1
            if self.counts[x] > self.most:
                self.most = self.counts[x]
                self.mode = x
        return x

    def sym_dec(self, x):
        if x != '?' and x in self.counts:
            self._ent = None
            if self.n > 0:
                self.n -= 1
                self.counts[x] -= 1
        return x

    def sym_ent(self):
        if not self._ent:
            self._ent = 0
            for n in self.counts.values():
                p = n / self.n
                self._ent -= p * log2(p)
        return self._ent


if __name__ == '__main__':
    pass
