# Table Reader

import re, traceback


class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            print("\t")
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


# ----- data ----------------------------

DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


# ----- readers ----------------------------

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


# ----- test cases ----------------------------

def ok0(src):
    for row in prep(cols(rows(lines(src)))):
        print(row)


@O.k
def ok1():
    ok0(DATA1)


@O.k
def ok2():
    ok0(DATA2)