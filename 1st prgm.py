import pandas as pd
df = pd.read_csv("student.csv")

#print(df)

# print 1st five data's
print(df.head())

# display last five data's
print(df.tail())

# display last 6 data's
print(df.tail(6))

# info - print the information about the dataset
print(df.info())
