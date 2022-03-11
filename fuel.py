import pandas as pd
df = pd.read_csv("fuel.csv")
# print 1st five data's
print(df.head())
# display 1st 8 data's
print(df.head(8))
# display last five data's
print(df.tail())
# info print the information about the dataset
print(df.info())