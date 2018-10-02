from prettytable import PrettyTable

from utils.test_rig import O
from w4.src.data import Data
from w5.src.unsuper import unsuper


def print_data(headers, rows, title):
    table = PrettyTable(title=title)
    table.field_names = headers
    for r in rows:
        table.add_row(r)
    print('\n')
    print(table)


@O.k
def unsuper_descretized():
    data = unsuper(Data(file='../data/weatherLong.csv'))
    headers = []
    for _, c in data.names.items():
        headers.append(c)
    print_data(headers, data.rows, title='weatherLong.csv')
