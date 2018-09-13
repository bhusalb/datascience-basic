import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('logistic_regression_dataset.csv')

del df['Cabin']
del df['Ticket']
del df['Name']
del df['PassengerId']

encoder = LabelEncoder()

print(df['Sex'].unique())
encoder.fit(df['Sex'])

df['Sex'] = encoder.transform(df['Sex'])
print(df['Embarked'].unique())
df1 = pd.get_dummies(df['Embarked'])
master_df = pd.concat([df, df1], axis=1)

master_df['Age'] = master_df['Age'].fillna(master_df['Age'].mean())

del master_df['Embarked']

Y = master_df['Survived']
X = master_df.drop('Survived', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))

from sklearn.tree import DecisionTreeClassifier, export_graphviz

t = DecisionTreeClassifier(criterion='entropy')

t.fit(X_train, y_train)

y_pred = t.predict(X_test)

print(accuracy_score(y_test, y_pred))

# print(X_train.columns)
export_graphviz(t)

from sklearn.svm import SVC

svm = SVC(C=5)

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

print(accuracy_score(y_test, y_pred))
