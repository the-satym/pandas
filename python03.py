import pandas as pd
# get to know how big the dataset is
#df.shape()

#what are the names of columns in the dataset

df= pd.read_csv("marks_final.csv")

# print(df.shape)
# print(df.columns)

#operations on columns
#selecting a specific column
column = df['ROLL NUMBER', 'SNO.']
print(column)


#filter rows based on a condition


#combine multiple conditions
