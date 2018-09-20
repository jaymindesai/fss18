# @author: Tim Menzies

import re
import sys
import zipfile


def lines(s=None, f=None):
    """Return contents, one line at a time."""
    if not s:
        for line in sys.stdin:
            yield line
    elif s[-3:] == "zip":  # <== warning, this clause not tested
        with zipfile.ZipFile(s) as z:
            with z.open(f, 'rt') as f:
                for line in f:
                    yield line
    elif s[-3:] in ["csv", "dat"]:
        with open(s) as fs:
            for line in fs:
                yield line
    else:
        for line in s.splitlines():
            yield line


def rows(src):
    """Kill bad characters. If line ends in ','
     then join to next. Skip blank lines."""
    cache = []
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cache += [line]
        if len(line) > 0:
            if line[-1] != ",":
                line = ''.join(cache)
                cache = []
                yield line


def cols(src, uses=None):
    """ If a column name on row1 contains '?',
    then skip over that column."""
    for row in src:
        cells = row.split(",")
        uses = uses or [False if "?" in s[0] else True for s in cells]
        out = [cells[pos] for pos, use in enumerate(uses) if use]
        yield out


def prep(src, nums=None):
    """ If a column name on row1 contains '$',
    coerce strings in that column to a float."""
    for xs in src:
        if nums:
            xs = [(float(x) if num else x) for x, num in zip(xs, nums)]
        else:
            nums = ["$" in x[0] for x in xs]
        yield xs
