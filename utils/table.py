from prettytable import PrettyTable


def print_table(headers, rows, title):
    table = PrettyTable(title=title)
    table.field_names = headers
    for r in rows:
        table.add_row(r)
    print('\n')
    print(table)
