import re
from w3.src.num import Num
from w3.src.sym import Sym


class Data:

    def __init__(self):
        self.w = {}  # weights of columns
        self.name = {}  # names of columns
        self.rows = {}  # data in tabular form - using dictionary instead of a 2D array for faster retrieval
        self.syms = {}  # data of symbol type columns
        self. nums = {}  # data of number type columns
        self.clazz = None  # classifier column
        self._use = {}  # columns in use => {col_in_data : col_in_csv}
        self.indeps = []  # independent columns

    def header(self, cells):
        """Parse columns from header row and update metadata"""
        for i, col in enumerate(cells[0]):
            if not re.match('[#?]', col):
                c = len(self._use) + 1
                self._use[c] = i  # c = col number in data, i = index of col in csv file
                self.name[c] = col
                if re.match('[<>%$]', col):
                    self.nums[c] = Num()
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
        """Add rows to data"""
        r = len(self.rows)
        self.rows[r] = []
        for col, col_csv in self._use.items():
            x = cells[col_csv]
            if not re.search('\?', x):
                if self.nums.get(col) is not None:
                    x = float(x)
                    self.nums[col].num_inc(x)
                else:
                    self.syms[col].sys_inc(x)
            self.rows[r][col] = x
