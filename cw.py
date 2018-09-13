import pandas as pd
from pandasql import sqldf

school_df = pd.read_csv('schools.csv')
student_df = pd.read_csv('students.csv')

school_df.info()
student_df.info()


def school_type_converter(item):
    if item == 1:
        return 'Public'
    else:
        return 'Private'


def sex_converter(item):
    if item == 1:
        return 'Male'
    else:
        return 'Female'


school_df['stype'] = school_df['stype'].apply(school_type_converter)
student_df['sex'] = student_df['sex'].apply(sex_converter)

data = sqldf(
    " select stype, sex, student_df.id from student_df "
    " join school_df on student_df.school_id = school_df.id ",
    locals())

pivot = pd.pivot_table(data, values='id',
                       columns='stype', index='sex', aggfunc=len)
