from math import pow

from w3.src.num import Num
from w4.src.data import Data

UNSUP_ENOUGH = 0.5
UNSUP_MARGIN = 1.05


def unsuper(data: Data):
    """Discretizing independent continuous numeric columns"""
    rows = data.rows
    most = 0
    enough = pow(len(rows), UNSUP_ENOUGH)
    margin = UNSUP_MARGIN

    def band(c, lo, hi):
        """Combine values falling in the same sd interval"""
        if lo == 0:
            return '..' + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + '..'
        else:
            return str(rows[lo][c]) + '..' + str(rows[hi][c])

    def argmin(c, lo, hi):
        """Determine the cut"""
        cut = None
        if (hi - lo) > 2 * enough:
            l, r = Num(), Num()
            for i in range(lo, hi):
                r.num_inc(rows[i][c])
            best = r.sd
            for i in range(lo, hi):
                x = rows[i][c]
                l.num_inc(x)
                r.num_dec(x)
                if l.n >= enough and r.n >= enough:
                    temp = l.num_xpect(r) * margin
                    if temp < best:
                        cut, best = i, temp
        return cut

    def cuts(c, lo, hi, pre):
        """Based on the cuts, replace column values with discretized intervals"""
        txt = pre + str(rows[lo][c]) + '..' + str(rows[hi][c])
        cut = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + '|.. ')
            cuts(c, cut + 1, hi, pre + '|.. ')
        else:
            b = band(c, lo, hi)
            print(txt + ' (' + b + ')')
            for i in range(lo, hi + 1):
                rows[i][c] = b

    def stop(c):
        """Determine where to stop"""
        for i in range(len(rows) - 1, -1, -1):
            if rows[i][c] != '?':
                return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows.sort(key=lambda x: 10 ** 32 if x[c] == '?' else x[c])  # Sort to push all the '?' to the end
            most = stop(c)
            print('\n' + str(data.names[c] + ', most = ' + str(most) + '\n'))
            cuts(c, 0, most, '|.. ')
            data.names[c] = data.names[c][1:]

    replace_discretized_columns(data, rows)
    return data


def replace_discretized_columns(data, rows):
    for i in range(len(rows)):
        data.rows[i] = rows[i]