import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('hr_data.csv', delimiter=';')

encoder = LabelEncoder()

encoder.fit(df['sales'])

df['sales1'] = encoder.transform(df['sales'])