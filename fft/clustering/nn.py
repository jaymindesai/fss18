from functools import reduce

import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors



df1 = pd.read_csv('../data/CSV/DataClass/_data-class.csv')
df2 = pd.read_csv('../data/CSV/FeatureEnvy/_feature-envy.csv')
df3 = pd.read_csv('../data/CSV/GodClass/_god-class.csv')
df4 = pd.read_csv('../data/CSV/LongMethod/_long-method.csv')

to_drop_data_god = ['$isStatic_type']
to_drop_feature_long = ['$isStatic_type', '$isStatic_method']

df1.drop(columns=to_drop_data_god, inplace=True)
df3.drop(columns=to_drop_data_god, inplace=True)
df2.drop(columns=to_drop_feature_long, inplace=True)
df4.drop(columns=to_drop_feature_long, inplace=True)


X_train = df4.drop(columns=['SMELLS'])

nn = NearestNeighbors(n_neighbors=3, metric='euclidean')

nn.fit(X_train)

distances, indices = nn.kneighbors(X_train)

# print(distances)
# print(indices)

sum = []
for d in distances:
    sum.append(reduce(lambda x, y: x + y, d) / (len(d) - 1))

frame = pd.DataFrame(sum)
print(frame.describe())
print('')
nptile = 90
print('{}th Percentile => {}'.format(nptile, np.percentile(frame.values, nptile)))

# print(sum/len(distances))