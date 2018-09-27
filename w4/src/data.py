import re
from w3.src.num import Num
from w3.src.sym import Sym
from utils.reader import rows, lines, cols


class Data:

    def __init__(self, file=None):
        self.w = {}  # weights of columns
        self.names = {}  # names of columns
        self.rows = {}  # data in tabular form - using dictionary instead of a 2D array for faster retrieval
        self.syms = {}  # data of symbol type columns
        self.nums = {}  # data of number type columns
        self.clazz = None  # classifier column
        self._use = {}  # columns in use => {col_in_data : col_in_csv}
        self.indeps = []  # independent columns
        if file:
            self.add_rows(file)

    def header(self, cells):
        """Parse columns from header row and update metadata"""
        for i, col in enumerate(cells):
            if not re.match('\?', col):
                c = len(self._use) + 1
                self._use[c] = i  # c = col number in data, i = index of col in csv file
                self.names[c] = col
                if re.match('[<>$]', col):
                    self.nums[c] = Num()
                else:
                    self.syms[c] = Sym()
                if re.match('<', col):
                    self.w[c] = -1
                elif re.match('>', col):
                    self.w[c] = 1
                elif re.match('!', col):
                    self.clazz = c
                else:
                    self.indeps.append(c)

    def row(self, cells):
        """Add rows to Data"""
        r = len(self.rows)
        self.rows[r] = []
        for col, col_csv in self._use.items():
            x = cells[col_csv]
            if not re.search('\?', x):
                if self.nums.get(col) is not None:
                    x = float(x)
                    self.nums.get(col).num_inc(x)
                else:
                    self.syms.get(col).sym_inc(x)
            self.rows[r].append(x)

    def col(self, cells):
        """Returns the list of column data to be appended to existing rows"""
        temp = []
        for i, x in enumerate(cells):
            if not re.search('\?', x):
                if self.nums.get(i + len(self.names)) is not None:
                    x = float(x)
                    self.nums.get(i + len(self.names)).num_inc(x)
                else:
                    self.syms.get(i + len(self.names)).sym_inc(x)
            temp.append(x)
        return temp

    def add_rows(self, file):
        """Cleans the data in file and populates Data object with header and rows"""
        for i, row in enumerate(cols(rows(lines(s=file)))):
            if i == 0:
                self.header(row)
            else:
                self.row(row)
        return self

    def add_cols(self, file):
        """Appends new column data to existing rows"""
        col_data = []
        for i, to_append in enumerate(cols(rows(lines(s=file)))):
            if i == 0:
                self.header(to_append)
            else:
                col_data.append(self.col(to_append))
        for i in range(0, len(col_data)):
            self.rows[i] += col_data[i]
        return self


if __name__ == '__main__':
    pass
