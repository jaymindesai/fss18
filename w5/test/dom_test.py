from utils.table import print_table
from utils.test_rig import O
from w4.src.data import Data
from w5.src.dom import dom_score


@O.k
def weather_dom_scores():
    """print the rows in descending order of their dom score"""
    data = Data(file='../data/weatherLong.csv')
    data = dom_score(data)
    data.rows.sort(key=lambda x: x[-1], reverse=True)
    print_table(data.names.values(), data.rows, title='weatherLong.csv')


@O.k
def auto_dom_scores():
    """print the first and last 10 rows in descending order of their dom score"""
    data = Data(file='../data/auto.csv')
    data = dom_score(data)
    data.rows.sort(key=lambda x: x[-1], reverse=True)
    rows = data.rows[:10] + data.rows[-10:]
    print_table(data.names.values(), rows, title='auto.csv')
