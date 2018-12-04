import pandas as pd
from sklearn.cluster import KMeans

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

# dfs_elbow = {'Data Class': [df1, 3], 'Feature Envy': [df2, 4], 'God Class': [df3, 4], 'Long Method': [df4, 4]}
# dfs_slt = {'Data Class': [df1, 4], 'Feature Envy': [df2, 8], 'God Class': [df3, 6], 'Long Method': [df4, 9]}

under_obs = {'Data Class': [df1, 3]}

for name, props in under_obs.items():
    df, k = props
    labels = df['SMELLS']
    data = df.drop(columns=['SMELLS'])

    kmeans = KMeans(n_clusters=k, random_state=0, precompute_distances=True, verbose=0, n_jobs=-1).fit(data)

    X_df = pd.DataFrame({'cluster': kmeans.labels_, 'label': labels.values})

    n_pure_clusters = 0
    points_covered_in_pure_clusters = 0

    print('Code Smell:', name, '|', 'Number of clusters:', k)
    for c in range(k):
        print('\t')
        print('Cluster: {}'.format(c))
        points = X_df[X_df['cluster'] == c]
        counts = len(points)
        vc = points['label'].value_counts()
        if len(vc) == 1:
            pure = 'YES'
        else:
            pure = 'YES' if min(vc)/counts <= 0.1 else 'NO'
        for i in vc.index:
            print('{}:'.format(i), vc[i])
        print('Homogeneous:', pure)
        if pure is 'YES':
            n_pure_clusters += 1
            points_covered_in_pure_clusters += counts

    print('')
    print('Number of Homogeneous Clusters:', n_pure_clusters)
    print('Points covered in homogeneous clusters:', round(points_covered_in_pure_clusters/len(data) * 100, 2), '%')
    print('\t')
    print('------')
    print('\t')


# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df['SMELLS'])
