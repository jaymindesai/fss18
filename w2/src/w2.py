# Table Reader

import re


def lines(src):
    """Return contents, one line at a time.

     Killing the blank lines/spaces and # followed
     substrings here to avoid iterations on list
     of lines in the subsequent methods. Performing
     cleanup on raw data seems to be faster compared
     to the case when cleanup is performed on list
     of lines."""

    pattern = re.compile('#(.*)')

    return pattern.sub("", src) \
        .replace(" ", "") \
        .split()


def rows(src):
    """If line ends in ',' then join to next."""

    for i, row in enumerate(src):
        if str(row).endswith(','):
            src[i] += src.pop(i + 1)
            rows(src)

    return src


def cols(src):
    """If a column name on row1 contains '?',
     then skip over that column."""

    index = get_index('?', src[0].split(','))

    for i, row in enumerate(src):
        row = row.split(',')
        del row[index]
        src[i] = row

    return src


def prep(src):
    """If a column name on row1 contains '$',
     coerce strings in that column to a float."""

    index = get_index('$', src[0])

    for row in src[1:]:
        row[index] = float(row[index])

    return src


def get_index(char, data):
    for i, row in enumerate(data):
        if str(row).startswith(char):
            return i

