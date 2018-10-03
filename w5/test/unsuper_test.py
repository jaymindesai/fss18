from utils.table import print_table
from utils.test_rig import O
from w4.src.data import Data
from w5.src.unsuper import unsuper


@O.k
def unsuper_descretized():
    data = unsuper(Data(file='../data/weatherLong.csv'))
    print_table(data.names.values(), data.rows, title='weatherLong.csv')
