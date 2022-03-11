import pandas as pd

# skiprows - used to skip the rows
df = pd.read_csv("student.csv", skiprows=[0, 2])

print(df)
