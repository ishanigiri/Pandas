import pandas as pd
data1 = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
}
data2 = {
    "ID": [2, 3, 4],
    "Score": [85, 90,88]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
#Merge the two DataFrames on thr ID column
merged_df = pd.merge(df1, df2, on="ID", how="inner")
print("Merged DataFrame:")
print(merged_df)