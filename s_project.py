import pandas as pd
import sqlite3
connection = sqlite3.connect("student.db")
df = pd.read_sql_query("select * from student")
print(df)
