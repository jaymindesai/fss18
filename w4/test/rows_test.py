import re
from csv import reader

from utils.test_rig import O
from w4.src.rows import Data


@O.k
def test_weather():
    """Testing weather.csv"""
    with open("../data/weather.csv") as csv_file:
        d = reader(csv_file)
        for row in d:
            for _, v in enumerate(row):
                if re.match(r"%?", v):
                    print(v)