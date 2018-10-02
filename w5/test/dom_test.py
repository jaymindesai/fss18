from prettytable import PrettyTable

from utils.test_rig import O
from w4.src.data import Data
from w5.src.dom import dom_score


def print_data(headers, rows, title):
    table = PrettyTable(title=title)
    table.field_names = headers
    for r in rows:
        table.add_row(r)
    print(table)


def sort_rows(rows):
    """Some extra effort to sort rows as rows is a dictionary"""
    for r in rows:
        r[-1] = round(r[-1], 2)
    rows.sort(key=lambda x: x[-1], reverse=True)
    return rows


@O.k
def weather_dom_scores():
    """print the rows in descending order of their dom score"""
    data = Data(file='../data/weatherLong.csv')
    data = dom_score(data)
    headers = []
    for _, c in data.names.items():
        headers.append(c)
    print_data(headers, sort_rows(data.rows), title='weatherLong.csv')


@O.k
def auto_dom_scores():
    """print the first and last 10 rows in descending order of their dom score"""
    data = Data(file='../data/auto.csv')
    data = dom_score(data)
    headers = []
    for _, c in data.names.items():
        headers.append(c)
    rows = sort_rows(data.rows)
    rows = rows[:10] + rows[-10:]
    print_data(headers, rows, title='auto.csv')



