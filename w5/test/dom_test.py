from prettytable import PrettyTable
from utils.test_rig import O
from w4.src.data import Data
from w5.src.dom import Dom


dom = Dom()


def print_data(headers, rows, title):
    table = PrettyTable(title=title)
    table.field_names = headers
    for r in rows:
        table.add_row(r)
    print(table)


def sort_rows(rows):
    to_sort = []
    for _, r in rows.items():
        to_sort.append(r)
        r[-1] = round(r[-1], 2)
    to_sort.sort(key=lambda x: x[-1], reverse=True)
    return to_sort


@O.k
def weather_dom_scores():
    """print the rows in descending order of their dom score"""
    data = Data(file='../data/weatherLong.csv')
    data = dom.dom_score(data)
    headers = []
    for _, c in data.names.items():
        headers.append(c)
    print_data(headers, sort_rows(data.rows), title='weatherLong.csv')


@O.k
def auto_dom_scores():
    """print the rows in descending order of their dom score"""
    data = Data(file='../data/auto.csv')
    data = dom.dom_score(data)
    headers = []
    for _, c in data.names.items():
        headers.append(c)
    rows = sort_rows(data.rows)
    rows = rows[:10] + rows[-10:]
    print_data(headers, rows, title='auto.csv')



