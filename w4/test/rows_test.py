from prettytable import PrettyTable
from utils.test_rig import O
from utils.reader import rows, lines, cols
from w4.src.rows import Data


def print_table(table: Data):
    """Prints all Num and Sym data in a tabular format."""
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


def prep_table(file):
    """Cleans the data in csv file and populates Data object with header and rows."""
    table_data = Data()
    file_data = cols(rows(lines(s=file)))
    for i, row in enumerate(file_data):
        if i == 0:
            table_data.header(row)
        else:
            table_data.row(row)
    return table_data


@O.k
def weather_stats():
    table = prep_table('../data/weather.csv')
    print_table(table)


@O.k
def weatherLong_stats():
    table = prep_table('../data/weatherLong.csv')
    print_table(table)


@O.k
def auto_stats():
    table = prep_table('../data/auto.csv')
    print_table(table)