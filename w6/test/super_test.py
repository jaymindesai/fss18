from utils.table import print_table
from utils.test_rig import O
from w4.src.data import Data
from w6.src.super import superr


@O.k
def weatherLong_super_descretized():
    data = superr(Data(file='../data/weatherLong.csv'))
    print_table(data.names.values(), data.rows, title='weatherLong.csv')


@O.k
def auto_super_descretized():
    superr(Data(file='../data/auto.csv'))
