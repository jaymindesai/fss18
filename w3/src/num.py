from math import pow, sqrt

from w3.src.sample import Sample


class Num:

    def __init__(self, mx=1024):
        self.mx = mx
        self.n = 0
        self.mu = 0
        # TODO: What is m2?
        self.m2 = 0
        self.sd = 0
        self.lo = pow(10, 32)
        self.hi = pow(10, -32)
        self.w = 1
        self._some = Sample(mx)

    def nums(self, nums, func=None):
        f = func and func or (lambda x: x)
        if nums:
            for num in nums:
                self.num_inc(f(num))
        return self

    def num_inc(self, x):
        if x != '?':
            self.n += 1
            self._some.sample_inc(x)
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            if x > self.hi:
                self.hi = x
            if x < self.lo:
                self.lo = x
            if self.n >= 2:
                self.sd = sqrt(self.m2 / (self.n - 1 + pow(10, -32)))
        return x

    def num_dec(self, x):
        if x != '?' and self.n != 1:
            self.n -= 1
            d = x - self.mu
            self.mu -= d / self.n
            self.m2 -= d * (x - self.mu)
            # TODO: Can this be negative?
            self.m2 = abs(self.m2)
            if self.n >= 2:
                self.sd = sqrt(self.m2 / (self.n - 1 + pow(10, -32)))
        return x

    def num_norm(self, x):
        return x is '?' and 0.5 or (x - self.lo) / (self.hi - self.lo + pow(10, -32))

    def num_xpect(self, other):
        total = self.n + other.n + pow(10, -32)
        return (self.n / total * self.sd) + (other.n / total * other.sd)


if __name__ == '__main__':
    pass
