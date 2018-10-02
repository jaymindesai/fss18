from prettytable import PrettyTable

from utils.test_rig import O
from w4.src.data import Data


def print_table(table: Data):
    """Prints all Num and Sym data in a tabular format"""
    print("\n")
    sym_table = PrettyTable(title="symbolic attributes")
    sym_table.field_names = ['col_index', 'col_name', 'n', 'mode', 'frequency']

    num_table = PrettyTable(title="numeric attributes")
    num_table.field_names = ['col_index', 'col_name', 'n', 'mu', 'sd']

    nums = table.nums
    syms = table.syms
    columns = table.names

    for i, col in columns.items():
        if i in nums:
            num_table.add_row([i, col, nums[i].n, nums[i].mu, nums[i].sd])
        else:
            sym_table.add_row([i, col, syms[i].n, syms[i].mode, syms[i].most])

    print(sym_table)
    print(num_table)


@O.k
def weather_stats():
    print_table(Data(file='../data/weather.csv'))


@O.k
def weatherLong_stats():
    print_table(Data(file='../data/weatherLong.csv'))


@O.k
def auto_stats():
    print_table(Data(file='../data/auto.csv'))