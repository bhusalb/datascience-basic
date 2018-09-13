from pandasql import sqldf
import pandas as pd

employee_data = pd.read_csv('hr_data.csv', delimiter=';')

limited_data = sqldf("SELECT sales, salary, count(*) as emp_count FROM employee_data "
                     " GROUP BY sales, salary order by emp_count DESC ", locals())
