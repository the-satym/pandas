import pandas as pd
# get to know how big the dataset is
#df.shape()

#what are the names of columns in the dataset

df= pd.read_csv("marks_final.csv")

# print(df.shape)
# print(df.columns)

#operations on columns
#selecting a specific column
column = df[['ROLL NUMBER', 'SNO.']]
print(column)

print(df["ROLL NUMBER"])

#filter rows based on a condition

rows = df[(df['SNO.']>1000) & (df['SNO.']<1050)]
rows = df[(df['SNO.']>1000) | (df['SNO.']<1050)]
rows2 = df[df['ROLL NUMBER'] == 102203794]

print(rows)
print(rows2)



#combine multiple conditions
