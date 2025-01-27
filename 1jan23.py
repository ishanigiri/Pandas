import pandas as pd
import numpy as np 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 30, 35],
    "City": ["Newyork", "Los Angeles", "Chicago", "None"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)
print("\nDataFrame after filling missing values:")
print(df)
#Drop rows with missing values
df = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df)
