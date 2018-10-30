import re
from itertools import islice
from math import inf

import pandas as pd
import scipy.stats as stats


def entropy(attribute: pd.Series):
    """Calculate Entropy"""
    counts = attribute.value_counts()
    prob = counts / len(attribute)
    return stats.entropy(prob, base=2)


def information_gain(column_name, data: pd.DataFrame):
    """Calculate Information Gain"""
    data.sort_values(by=column_name, inplace=True)
    column_values = data[column_name]
    ent_class = entropy(data['class'])  # Entropy of Class
    total = len(column_values)
    min_ent = inf
    cut = None
    if re.match('\$', column_name):
        # Calculate IG of continuous attributes
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
                cut = row[column_name]
        return ent_class - min_ent, cut
    else:
        # Calculate IG of discrete attributes
        counts = column_values.value_counts()
        cond_ent = 0
        for c in counts.index:
            weight = counts[c] / total
            ent = entropy(data[column_values == c]['class'])
            cond_ent += weight * ent
            if ent < min_ent:
                min_ent = ent
                cut = c
        return ent_class - cond_ent, cut


def find_split(data):
    info_gains = {}
    for column in data.columns[:-1]:
        gain, cut = information_gain(column, data)
        print('\n')
        print('Feature:', column)
        print('\n')
        print(data.sort_values(by=column)[[column, 'class']])
        print('\n')
        print('Info Gain:', gain, '| Cut:', cut)
        print('\n')
        print('-----------------------------------------------')
        info_gains[column] = (gain, cut)
    print('\n')
    print('Info Gains:', info_gains)


df = pd.read_csv('data/weather.csv')
find_split(df)


