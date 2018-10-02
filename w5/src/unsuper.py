from math import pow

from w3.src.num import Num
from w4.src.data import Data

UNSUP_ENOUGH = 0.5
UNSUP_MARGIN = 1.05


def unsuper(data: Data):
    rows = data.rows
    enough = pow(len(rows), UNSUP_ENOUGH)
    margin = UNSUP_MARGIN

    def band(c, lo, hi):
        if lo == 1:
            return '..' + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + '..'
        else:
            return str(rows[lo][c]) + '..' + str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        if (hi - lo) > 2 * enough:
            l, r = Num(), Num()
            for i in range(lo, hi + 1):
                r.num_inc(rows[i][c])
            best = r.sd
            for i in range(lo, hi + 1):
                x = rows[i][c]
                l.num_inc(x)
                r.num_dec(x)
                if l.n >= enough and r.n >= enough:
                    temp = l.num_xpect(r) * margin
                    if temp < best:
                        cut, best = i, temp
        return cut

    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c]) + '.. ' + str(rows[hi][c])
        cut = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + '|.. ')
            cuts(c, cut + 1, hi, pre + '|.. ')
        else:
            b = band(c, lo, hi)
            print(txt + ' (' + b + ')')
            for r in range(lo, hi + 1):
                rows[r][c] = b

    def stop(c, rs):
        for i in range(len(rs) - 1, 1, -1):
            if not rs[i][c] == '?':
                return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows.sort(key=lambda x: 10 ** 32 if x[c] == '?' else x[c])
            most = stop(c, rows)
            print('\n________ most(' + str(data.names[c] + ') = ' + str(most) + ' ________\n'))
            cuts(c, 1, most, '|.. ')
            data.names[c] = data.names[c][1:]

    replace_discretized_column(data, rows)
    return data


def replace_discretized_column(data, rows):
    for i in range(len(rows)):
        data.rows[i] = rows[i]
