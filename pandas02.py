import pandas as pd

#display data

df = pd.read_csv("marks_final.csv", encoding="utf-8" )

print("display top 10 rows of data ")
print(df.head(1))
print("display bottom 10 rows of data ")
print(df.tail(1))

#display the info of dataset

print(df.info())

#discribe the dataset for numerical columns

print("descriptive stats of numerical columns")
print(df.describe())

