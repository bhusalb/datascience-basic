import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

df = pd.read_csv('a.csv')

print(df['MaxTemp'].shape)
x = df['MaxTemp'].values.reshape(-1, 1)
y = df['MinTemp'].values.reshape(-1, 1)

print(x.shape)

X, X_TEST, Y, Y_TEST = train_test_split(x, y, test_size=0.33)

model = LinearRegression()

model.fit(X, Y)

Y_P = model.predict(X_TEST)

print(mean_squared_error(Y_TEST, Y_P))

print(r2_score(Y_TEST, Y_P))

print(model.predict(30))

plt.scatter(X_TEST, Y_TEST, color='blue', marker='.')
plt.scatter(X_TEST, Y_P, color='red', marker='.')

plt.show()
