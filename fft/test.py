import re
from itertools import islice
from math import inf

import pandas as pd
import scipy.stats as stats

df = pd.read_csv('data/weather.csv')

df = df[['$temp', 'class']]

print(df.sort_values(by='$temp'))


def entropy(attribute: pd.Series):
    counts = attribute.value_counts()
    prob = counts / len(attribute)
    return stats.entropy(prob, base=2)


def calculate_ig(column_name, data: pd.DataFrame):
    h_clazz = entropy(data['class'])
    if re.match('\$', column_name):
        data.sort_values(by=column_name, inplace=True)
        min_ent = inf
        split = None
        prev = 0
        first = 1
        last = len(data) - 1
        for _, i in islice(data.iterrows(), first, last):
            df1 = data[data[column_name] < i[0]]
            df2 = data[data[column_name] >= i[0]]
            ent1 = entropy(df1['class'])
            ent2 = entropy(df2['class'])
            weight1 = df1[column_name].count() / data[column_name].count()
            weight2 = df2[column_name].count() / data[column_name].count()
            cond_ent = (weight1 * ent1) + (weight2 * ent2)
            if cond_ent < min_ent:
                min_ent = cond_ent
                split = i[0]
            print('---------------------------')
            print('$temp ' + str(i[0]))
            print('\t')
            print('Entropy for $temp < ' + str(i[0]) + ': ' + str(round(ent1, 4)))
            print('Entropy for $temp >= ' + str(i[0]) + ': ' + str(round(ent2, 4)))
            print('\t')
            print('Conditional Entropy for split between $temp = ' + str(prev) + ' and $temp = ' + str(
                i[0]) + ' is ' + str(
                round(cond_ent, 4)))
            print('\t')
            prev = i[0]
        print('---------------------------')
        print('\t')
        print('Split at $temp =  ' + str(split))
        print('\t')
    else:
        column_values = data[column_name]
        total = len(column_values)
        counts = column_values.value_counts()
        cond_ent = 0
        for c in counts.index:
            weight = counts[c] / total
            ent = entropy(data[data[column_name] == c]['class'])
            cond_ent += weight * ent
        return h_clazz - cond_ent


ig = {}
for column in df.columns[:-1]:
    ig[column] = calculate_ig(column, df)

print(ig)
