# Creating a class with function to calculate the domination score.
# Instead of adding this methods to Data class.

from math import pow
from w4.src.data import Data


class Dom:

    def dom(self, row1, row2, data):
        s1 = 0
        s2 = 0
        n = len(data.w)
        for c, w in data.w.items():
            a0 = row1[c - 1]
            b0 = row2[c - 1]
            a = data.nums[c].num_norm(a0)
            b = data.nums[c].num_norm(b0)
            s1 -= pow(10, (w * ((a - b)/n)))
            s2 -= pow(10, (w * ((b - a)/n)))
        return (s1 / n) < (s2 / n)

    def dom_score(self, data: Data):
        n = 100  # Default number of samples for Dom
        c = len(data.names) + 1
        data.names[c] = '>dom'
        for i in range(0, len(data.rows)):
            row1 = data.rows[i]
            row1.insert(c - 1, 0)
            for s in range(1, n+1):
                row2 = data.another(row1)
                s = self.dom(row1, row2, data) and 1/n or 0
                row1[c - 1] += s
            data.rows[i] = row1
        return data
