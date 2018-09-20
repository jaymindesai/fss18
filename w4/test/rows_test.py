import re
from csv import reader

from utils.test_rig import O
from w4.src.rows import Data


@O.k
def test_weather():
    """Testing weather.csv"""
    table_data = Data()
    with open("../data/weather.csv") as csv_file:
        file_data = reader(csv_file)
        for i, row in enumerate(file_data):
            if i == 0:
                table_data.header(row)
            else:
                table_data.row(row)
    print(table_data.names)

