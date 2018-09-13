import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('hr_data.csv', delimiter=';')

df.groupby(['sales', 'salary']).size().plot(kind='bar', stacked=False)
#
plt.show()

# df.groupby(['sales']).size().plot(kind='pie', title='Pie Chart of Department', label='Department', legend=True)

# df['satisfaction_level'].plot(kind='box', vert=False)
# plt.show()
