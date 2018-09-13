import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def salary_converter(salary):
    if salary == 'low':
        return 15000
    if salary == 'medium':
        return 45000
    if salary == 'high':
        return 100000


data = pd.read_csv('hr_data.csv', delimiter=';')
# head_data = data.head(5)
# tail_data = data.tail(5)
# data.info()
# describe_value = data.describe()
# satisfaction_level = data['satisfaction_level'].describe()
# print(satisfaction_level)
# another_satisfaction_level = data.satisfaction_level
# # print(type(satisfaction_level))
# two_columns = data[['satisfaction_level', 'salary']]
#
# middle_part = data.iloc[:50:2]
# a_middle_part = data.iloc[:500, [0, 1, 3]]
#
# query_data = data[(data['satisfaction_level'] > 0.9) & (data['average_montly_hours'] > 200)]
#
# # query_data = query_data['sales'].unique()
# print(data['salary'])
# # data['salary'] = data['salary'].apply(salary_converter)
#
# # data['satisfaction_level'] = data['satisfaction_level'] * 100
# data = data.sort_values(['satisfaction_level', 'last_evaluation'], ascending=[True, False])
#
# sample = data[data['satisfaction_level'] == 0.9]['satisfaction_level']

data_3 = data.groupby(['salary', 'sales'])['satisfaction_level'].mean()
print(data_3)

new_data = pd.pivot_table(data, index=['sales'], columns=['salary'], values='satisfaction_level', aggfunc=np.median)

print(new_data)