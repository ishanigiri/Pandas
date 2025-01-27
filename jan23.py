import pandas as pd 
#create a datafraame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Newyork", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
#Read data from a CSV file
#asume "data.csv" exists in the current directory
#df = pd.read_csv("data.csv")

#Display thr first few rows of the DataFrame
print("\nFirst 2 rows:")
print(df.head(2))
#Filter rows where Age> 25
filtered_df = df[df["Age"] > 25]
print("\nFiltered DataFrame:")
print(filtered_df)
# add a new column
df["Score"] = [85, 90, 88]
print("\nDataFrame with new column:")
print(df)
#save the DataFrame to a csv file
df.to_csv("output.csv", index=False)
print("\nData saved to output.csv")