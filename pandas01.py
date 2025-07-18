import pandas as pd
# # read data from a csv file into a pandas DataFrame
#
# df = pd.read_csv('data.csv', encoding="utf-8")
# df2= pd.read_json('data.json', encoding="latin-1")
#
# print(df)
# print(df2)

# create a new DataFrame with specific types
data = {"name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]}


df3 = pd.DataFrame(data)
df3.to_csv("info.csv", index=False, encoding="utf-8")
print("DataFrame saved to info.csv")