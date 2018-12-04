import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from sklearn.utils import shuffle
from sklearn.cluster import KMeans

import numpy as np

# df = pd.read_csv('data/CSV/DataClass/_data-class.csv')
df = pd.read_csv('data/CSV/FeatureEnvy/_feature-envy.csv')
# df = pd.read_csv('data/CSV/GodClass/_god-class.csv')
# df = pd.read_csv('data/CSV/LongMethod/_long-method.csv')

y = df['SMELLS']
X = df.drop(columns=['SMELLS'])

skfolds = StratifiedKFold(n_splits=10, random_state=100)

# clf = RandomForestClassifier(random_state=100, n_estimators=100)
clf = SVC(C=5, kernel='rbf', gamma='scale', random_state=100)
# clf = LinearSVC(random_state=100)

accuracy = []
balanced_accuracy = []

print(y.value_counts())
print('\t')

for train_index, test_index in skfolds.split(X, y):
    cloned_clf = clone(clf)

    X_train = X.iloc[train_index]
    y_train = y.iloc[train_index]

    X_test = X.iloc[test_index]
    y_test = y.iloc[test_index]

    cloned_clf.fit(X_train, y_train)

    y_pred = cloned_clf.predict(X_test)

    accuracy.append(round(accuracy_score(y_test, y_pred), 2))
    balanced_accuracy.append(round(balanced_accuracy_score(y_test, y_pred), 2))

print('Without Clustering...')
print(accuracy)
print(balanced_accuracy)
print('\t')

exp_acc = []
exp_bacc = []
for train_index, test_index in skfolds.split(X, y):
    cloned_clf = clone(clf)

    X_train = X.iloc[train_index]
    y_train = y.iloc[train_index]

    X_test = X.iloc[test_index]
    y_test = y.iloc[test_index]

    K = 4
    kmeans = KMeans(n_clusters=K, random_state=100, precompute_distances=True, verbose=0).fit(X_train)

    X_train = X_train.assign(cluster=kmeans.labels_)
    X_test = X_test.assign(cluster=kmeans.predict(X_test))

    y_true = []
    y_pred = []
    clusters = X_test['cluster'].value_counts().index
    for c in clusters:
        X_train_new = X_train[X_train['cluster'] == c]
        y_train_new = y_train[X_train_new.index.values]
        X_test_new = X_test[X_test['cluster'] == c]
        y_test_new = y_test[X_test_new.index.values]

        y_true.extend(y_test_new.values)

        cloned_clf.fit(X_train_new, y_train_new)

        y_pred.extend(cloned_clf.predict(X_test_new))

    exp_bacc.append(round(balanced_accuracy_score(y_true, y_pred), 2))
    exp_acc.append(round(accuracy_score(y_true, y_pred), 2))

print('With Clustering...')
print(exp_acc)
print(exp_bacc)
print('\t')



