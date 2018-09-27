from operator import itemgetter
from prettytable import PrettyTable
from utils.test_rig import O
from w4.src.data import Data
from w5.src.dom import Dom


@O.k
def weather_dom_scores():
    """print the rows in descending order of their dom score"""
    data = Data(file='../data/weatherLong.csv')
    dom = Dom()
    data = dom.dom_score(data)
    table = PrettyTable(title="weatherLong.csv")
    fields = []
    for _, c in data.names.items():
        fields.append(c)
    table.field_names = fields
    for _, r in data.rows.items():
        table.add_row(r)
    print(table)
