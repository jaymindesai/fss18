import pandas as pd
from sklearn.cluster import DBSCAN

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

# dfs_slt = {'Data Class': [df1, 4], 'Feature Envy': [df2, 8], 'God Class': [df3, 6], 'Long Method': [df4, 9]}
dfs = {'Long Method': [df4, 1000, 2]}

for name, props in dfs.items():
    df, eps, min_sam = props
    labels = df['SMELLS']
    data = df.drop(columns=['SMELLS'])

    # config = {
    #     'eps': list(range(1, 30)),
    #     'min_samples': list(range(5, 20)),
    #     'metric': ['euclidean', 'minkowski', 'cosine', 'cityblock'],
    #     'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
    # }

    dbs = DBSCAN(eps=eps, min_samples=min_sam, metric='euclidean', n_jobs=-1, algorithm='auto').fit(data)

    X_df = pd.DataFrame({'cluster': dbs.labels_, 'label': labels.values})

    N = len(X_df['cluster'].value_counts().index)
    n_pure_clusters = 0
    points_covered_in_pure_clusters = 0
    ignored = len(X_df[X_df['cluster'] == -1])
    print('Code Smell:', name, '|', 'Number of clusters:', N)
    for c in range(N):
        print('\t')
        print('Cluster: {}'.format(c))
        points = X_df[X_df['cluster'] == c]
        counts = len(points)
        vc = points['label'].value_counts()
        if len(vc) == 1:
            pure = 'YES'
        elif len(vc) > 0:
            pure = 'YES' if min(vc) / counts <= 0.1 else 'NO'
        else:
            pure = 'NO'
        for i in vc.index:
            print('{}:'.format(i), vc[i])
        print('Homogeneous:', pure)
        if pure is 'YES':
            n_pure_clusters += 1
            points_covered_in_pure_clusters += counts

    print('')
    print('Total Data Points:', len(data))
    print('Data Points Ignored', round((ignored / len(data) * 100), 2), '%')
    print('Total number of clusters:', N)
    print('Number of Homogeneous Clusters:', n_pure_clusters)
    print('Points covered in homogeneous clusters:', round(points_covered_in_pure_clusters / len(data) * 100, 2), '%')
    print('\t')
    print('------')
    print('\t')
