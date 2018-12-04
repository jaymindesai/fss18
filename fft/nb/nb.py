import pandas as pd
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('../data/CSV/DataClass/_data-class.csv')
to_drop = ['isStatic_type']

df.drop(columns=to_drop, inplace=True)

labels = df['SMELLS'].apply(lambda x: 0 if not x else 1)
data = df.drop(columns=['SMELLS'])

X_train, X_test, y_train, y_test = train_test_split(data, labels, stratify=labels, test_size=0.25)

nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

print(str(round(accuracy_score(y_test, y_pred), 2) * 100) + '%')