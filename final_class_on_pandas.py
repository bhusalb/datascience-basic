import pandas as pd
from matplotlib import pyplot as plt

school = pd.read_csv('schools.csv')
school['id'] = school['id'].astype('int')

student = pd.read_csv('students.csv')

merge_data = pd.merge(student, school, how='inner', left_on='school_id', right_on='id')

head_part = student.head(10)

tail_part = student.tail(10)

concat_data = pd.concat([head_part, tail_part])