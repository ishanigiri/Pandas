import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 90, 88, 75]
}
df = pd.DataFrame(data)
# sort by score in descending order
sorted_df = df.sort_values(by="Score", ascending=False)
print("DataFrame sorted by score:")
print(sorted_df)
#Add a rank column
df["rank"] = df["Score"].rank(ascending=False)
print("\nDataFramewith Rank:")
print(df)