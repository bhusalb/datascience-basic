import pandas as pd

df = pd.read_csv('voice.csv')

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df['label'] = encoder.fit_transform(df['label'])

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

Y = df['label']
X = df.drop('label', axis=1)

X = scaler.fit_transform(X)

from sklearn.svm import SVC

model = SVC(C=6)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred))

import numpy as np

t = [0.0597809849598081, 0.0642412677031359, 0.032026913372582, 0.0150714886459209, 0.0901934398654331,
     0.0751219512195122, 12.8634618371626, 274.402905502067, 0.893369416700807, 0.491917766397811, 0,
     0.0597809849598081, 0.084279106440321, 0.0157016683022571, 0.275862068965517, 0.0078125,
     0.0078125,
     0.0078125, 0, 0]
t = np.array([t])
t = scaler.transform(t)
print(t.shape)
output = model.predict(t)
inverse_output = encoder.inverse_transform(output)

from sklearn.linear_model import LogisticRegression

another_model = LogisticRegression()
another_model.fit(x_train, y_train)
y_a_pred = another_model.predict(x_test)
print(accuracy_score(y_a_pred, y_test))


