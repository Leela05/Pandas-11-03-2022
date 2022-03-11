import pandas as pd
df = pd.read_json("product.json")
print(df)
print(df.info())
print(df.head())
print(df.tail())