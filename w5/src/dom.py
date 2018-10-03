from math import pow

from w4.src.data import Data

DOM_SAMPLES = 100  # Default number of samples for Dom


def dom(row1, row2, data):
    s1, s2 = 0, 0
    n = len(data.w)
    for c, w in data.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = data.nums[c].num_norm(a0)
        b = data.nums[c].num_norm(b0)
        s1 -= pow(10, (w * ((a - b)/n)))
        s2 -= pow(10, (w * ((b - a)/n)))
    return (s1 / n) < (s2 / n)


def dom_score(data: Data):
    """Calculate the domination score for required columns"""
    n = DOM_SAMPLES
    c = len(data.names)
    data.names[c] = '>dom'
    for i in range(len(data.rows)):
        row1 = data.rows[i]
        row1.append(0)
        for j in range(n):
            row2 = data.another(row1)
            s = dom(row1, row2, data) and 1/n or 0
            row1[c] += s
        data.rows[i] = row1
        data.rows[i][-1] = round(data.rows[i][-1], 2)
    return data
