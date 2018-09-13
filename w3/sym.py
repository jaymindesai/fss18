from math import pow, log2


class Sym:

    def __init__(self):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

    def syms(self, f, symbols):
        f = lambda x: x if f is None else f
        if symbols:
            for symbol in symbols:
                self.sym_inc(f(symbol))

        return self

    def sym_inc(self, x):
        if x != '?':
            self._ent = None
            self.n += 1
            old = self.counts[x]
            new = old and old + 1 or 1
            self.counts[x] = new
            if new > self.most:
                self.most = new
                self.mode = x

        return x

    def sym_dec(self, x):
        if x != '?':
            self._ent = None
            if self.n > 0:
                self.n -= 1
                self.counts[x] -=1

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
