# Create a DataFrame with columns: Product, Price, and Quantity.
# Add a new column "Total" (Price * Quantity).
# Save the resulting DataFrame to a CSV file.

import pandas as pd 
#create a datafraame from a dictionary
data = {
    "Product": ["Fruits", "Vegetables", "Junk"],
    "Price": [250, 300, 635],
    "Quantity": [4, 5, 6]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
#Read data from a CSV file
#asume "data.csv" exists in the current directory
#df = pd.read_csv("data.csv")

#Display thr first few rows of the DataFrame
df["Total"] = df["Price"]*df["Quantity"]
print('\n Total Data:')
print(df)
#save the DataFrame to a csv file
df.to_csv("output.csv", index=False)
print("\nData saved to output.csv")