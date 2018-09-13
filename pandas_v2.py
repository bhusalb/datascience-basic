import pandas as pd


data = pd.read_csv('hr_data.csv', delimiter=';')

# df = data.groupby(['sales', 'salary'], as_index=True)

df1 = pd.pivot_table(data, values='satisfaction_level', index=['sales'], columns=['salary'])

df1.plot(x=0, y=-1, kind='bar', style='o')
