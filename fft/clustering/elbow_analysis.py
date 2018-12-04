import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from math import sqrt

# df = pd.read_csv('../data/CSV/DataClass/_data-class.csv')
# df = pd.read_csv('../data/CSV/FeatureEnvy/_feature-envy.csv')
# df = pd.read_csv('../data/CSV/GodClass/_god-class.csv')
df = pd.read_csv('../data/CSV/LongMethod/_long-method.csv')

# to_drop_data_god = ['$isStatic_type']
to_drop_feature_long = ['$isStatic_type', '$isStatic_method']

# df.drop(columns=to_drop_data_god, inplace=True)
df.drop(columns=to_drop_feature_long, inplace=True)

y = df['SMELLS']
X = df.drop(columns=['SMELLS']).values

clusters = int(sqrt(len(X)))

# mms = MinMaxScaler()
# mms.fit(X)
# data_transformed = mms.transform(X)
data_transformed = X

Sum_of_squared_distances = []
K = range(1, clusters)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data_transformed)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()