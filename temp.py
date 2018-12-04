import re
from itertools import islice
from math import inf

import pandas as pd
import scipy.stats as stats

df = pd.read_csv('data/weather.csv')

# df = df[['$temp', 'class']]


def entropy(attribute: pd.Series):
    counts = attribute.value_counts()
    prob = counts / len(attribute)
    return stats.entropy(prob, base=2)


def calculate_ig(column_name, data: pd.DataFrame):
    data.sort_values(by=column_name, inplace=True)
    h_clazz = entropy(data['class'])
    column_values = data[column_name]
    total = len(column_values)
    min_ent = inf
    split = None
    if re.match('\$', column_name):
        # prev = 0
        first = 1
        last = len(data) - 1
        for _, row in islice(data.iterrows(), first, last):
            df1 = data[column_values < row[column_name]]
            df2 = data[column_values >= row[column_name]]
            weight1 = df1[column_name].count() / total
            weight2 = df2[column_name].count() / total
            ent1 = entropy(df1['class'])
            ent2 = entropy(df2['class'])
            cond_ent = (weight1 * ent1) + (weight2 * ent2)
            if cond_ent < min_ent:
                min_ent = cond_ent
                split = row[column_name]
        #     print('---------------------------')
        #     print('$temp ' + str(row[column_name]))
        #     print('\t')
        #     print('Entropy for $temp < ' + str(row[column_name]) + ': ' + str(round(ent1, 4)))
        #     print('Entropy for $temp >= ' + str(row[column_name]) + ': ' + str(round(ent2, 4)))
        #     print('\t')
        #     print('Conditional Entropy for split between $temp = ' + str(prev) + ' and $temp = ' + str(
        #         row[column_name]) + ' is ' + str(
        #         round(cond_ent, 4)))
        #     print('\t')
        #     prev = row[column_name]
        # print('---------------------------')
        # print('\t')
        # print('Split at $temp =  ' + str(split))
        # print('\t')
        return h_clazz - min_ent, split
    else:
        counts = column_values.value_counts()
        cond_ent = 0
        for c in counts.index:
            weight = counts[c] / total
            ent = weight * entropy(data[column_values == c]['class'])
            cond_ent += ent
            if ent < min_ent:
                min_ent = ent
                split = c
        return h_clazz - cond_ent, split


info_gains = {}
for column in df.columns[:-1]:
    print(column)
    print('\n')
    print(df.sort_values(by=column)[[column, 'class']])
    print('\n')
    print('--------------------------------------------')
    print('\n')
    info_gains[column] = calculate_ig(column, df)

print('\n', info_gains)
