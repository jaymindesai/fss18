import re
from itertools import islice
from math import inf

import pandas as pd
import scipy.stats as stats

CLASS = 'SMELLS'

def entropy(attribute):
    """Calculate Entropy"""
    counts = attribute.value_counts()
    prob = counts / len(attribute)
    return stats.entropy(prob, base=2)


def information_gain(column_name, data):
    """Calculate Information Gain"""
    data.sort_values(by=column_name, inplace=True)
    column_values = data[column_name]
    ent_class = entropy(data[CLASS])  # Entropy of Class
    total = len(column_values)
    min_ent = inf
    cut = None
    if re.match('\$', column_name):
        # Calculate IG of discrete attributes
        counts = column_values.value_counts()
        cond_ent = 0
        for c in counts.index:
            weight = counts[c] / total
            ent = entropy(data[column_values == c][CLASS])
            cond_ent += weight * ent
            if ent < min_ent:
                min_ent = ent
                cut = c
        return ent_class - cond_ent, cut
    else:
        # Calculate IG of continuous attributes
        first = 1
        last = len(data) - 1
        for _, row in islice(data.iterrows(), first, last):
            df1 = data[column_values < row[column_name]]
            df2 = data[column_values >= row[column_name]]
            weight1 = df1[column_name].count() / total
            weight2 = df2[column_name].count() / total
            ent1 = entropy(df1[CLASS])
            ent2 = entropy(df2[CLASS])
            cond_ent = (weight1 * ent1) + (weight2 * ent2)
            if cond_ent < min_ent:
                min_ent = cond_ent
                cut = row[column_name]
        return ent_class - min_ent, cut


def find_cut(data):
    info_gains = {}
    for column in data.columns[:-1]:
        gain, cut = information_gain(column, data)
        print('\n')
        print('Feature:', column)
        print('\n')
        # print(data.sort_values(by=column)[[column, CLASS]])
        print('\n')
        print('Info Gain:', gain, '| Cut:', cut)
        print('\n')
        print('-----------------------------------------------')
        info_gains[column] = (gain, cut)
    print('\n')
    print('Info Gains:', info_gains)
    best = (-inf, None)
    feature = None
    for k, v in info_gains.items():
        if v[0] > best[0]:
            best = v
            feature = k
    print('\n')
    print('Best Feature:', feature, '| Cut:', best[1], '| Info Gain:', round(best[0], 4))


cfs = ['NOPK_project', 'NOI_project', 'LOC_project', 'number_not_final_static_methods', 'NOI_package',
       'NOCS_package', 'LOC_package', 'NOM_project', 'NOCS_project', CLASS]

wrapper_reptree = ['NOPK_project', 'number_standard_design_methods', 'LOC_project', 'NOCS_type', 'number_not_final_static_methods',
                   'NOM_project', 'NOAM_type', 'NOMNAMM_type', 'NOI_project', 'number_not_final_not_static_methods',
                   'NOCS_project', 'number_constructor_NotDefaultConstructor_methods', 'num_static_attributes',
                   'num_static_not_final_attributes', 'number_static_methods', 'NOM_type', 'number_protected_visibility_attributes',
                   'number_protected_visibility_methods', 'NMO_type', 'AMW_type', 'num_final_static_attributes', 'NOMNAMM_project', CLASS]

# df = pd.read_csv('data/CSV/DataClass/_data-class.csv')
# df = pd.read_csv('data/CSV/FeatureEnvy/_feature-envy.csv')
# df = pd.read_csv('data/CSV/GodClass/_god-class.csv')
df = pd.read_csv('data/CSV/LongMethod/_long-method.csv')
# df = df[cfs]
# df = df[wrapper_reptree]
find_cut(df)


