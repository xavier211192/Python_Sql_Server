from sqlalchemy import create_engine
import pandas as pd

#replace xavier with the dsn name created by you
engine = create_engine('mssql+pyodbc://xavier')
engine.execute("USE PX")  #Use your preferred database here
table_names = engine.table_names()
print(table_names)

#You can use any query here
df = pd.read_sql_query(" Select fname+lname as FullName from names ", engine)

print(df.head())