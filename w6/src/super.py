from math import pow, floor
from operator import itemgetter

from w3.src.num import Num
from w5.src.dom import dom_score

SUP_ENOUGH = 0.5
SUP_MARGIN = 1.05


def super(data):
    """Discretizing independent continuous numeric columns based on a particular goal"""
    data = dom_score(data)  # Add dom scores to data
    rows = data.rows
    goal = len(data.names) - 1
    most = 0
    enough = pow(len(rows), SUP_ENOUGH)
    margin = SUP_MARGIN
    splits = {}  # {column : {split : sd of dom for that split}}
    stdevs = {}  # {column : expected sd of column after split}

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
        xl, xr = Num(), Num()  # l, r for independent column
        yl, yr = Num(), Num()  # # l, r for goal column
        for i in range(lo, hi):
            xr.num_inc(rows[i][c])
            yr.num_inc(rows[i][goal])
        bestx = xr.sd  # sd of independent column for this split
        besty = yr.sd  # sd of goal for this split
        mu = yr.mu
        if (hi - lo) > 2 * enough:
            for j in range(lo, hi):
                x = rows[j][c]
                y = rows[j][goal]
                xl.num_inc(x)
                xr.num_dec(x)
                yl.num_inc(y)
                yr.num_dec(y)
                if xl.n >= enough and xr.n >= enough:
                    tempx = xl.num_xpect(xr) * margin
                    tempy = yl.num_xpect(yr) * margin
                    if tempx < bestx:
                        if tempy < besty:
                            cut, bestx, besty = j, tempx, tempy
        return cut, mu, besty

    def cuts(c, lo, hi, pre):
        """Based on the cuts, replace column values with discretized intervals"""
        txt = pre + str(rows[lo][c]) + '..' + str(rows[hi][c])
        cut, mu, dom_sd = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + '|.. ')
            cuts(c, cut + 1, hi, pre + '|.. ')
        else:
            b = band(c, lo, hi)
            splits[c][floor(100 * mu)] = dom_sd
            print(txt + ' ==> ' + str(floor(100 * mu)))
            for i in range(lo, hi + 1):
                rows[i][c] = b

    def stop(c):
        """Determine where to stop"""
        for i in range(len(rows) - 1, 0, -1):
            if rows[i][c] != '?':
                return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            splits[c] = {}
            rows.sort(key=lambda x: 10 ** 32 if x[c] == '?' else x[c])  # Sort to push all the '?' to the end
            most = stop(c)
            print('\n' + str(data.names[c] + ', most = ' + str(most) + '\n'))
            cuts(c, 0, most, '|.. ')
            data.names[c] = data.names[c][1:]

    replace_discretized_columns(data, rows)

    # Find Splitter
    for c, s in splits.items():
        n = sum(s.keys())
        expected_sd = 0
        for mu, sd in s.items():
            expected_sd += (mu / n) * pow(sd, 2)
        stdevs[c] = expected_sd

    splitter = data.names[sorted(stdevs.items(), key=itemgetter(1))[0][0]]

    print('\nAttribute with least expected Standard Deviation after splitting => \'' + splitter + '\'')

    return data


def replace_discretized_columns(data, rows):
    for i in range(len(rows)):
        data.rows[i] = rows[i]
        data.rows[i][-1] = round(data.rows[i][-1], 2)


if __name__ == '__main__':
    pass
