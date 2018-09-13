from random import random, seed
from math import pow

from utils.test_rig import O
from w3.src.sample import Sample


@O.k
def test_sample():
    seed(1)
    samples = []

    for i in range(5, 10):
        samples.append(Sample(pow(2, i)))

    for i in range(1, 10000):
        r = random()
        for s in samples:
            s.sample_inc(r)

    for s in samples:
        print(int(s.mx), s.nth(0.5))
        assert 0.3 < s.nth(0.5) < 0.7


