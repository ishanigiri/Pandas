# Load a CSV file containing student grades into a DataFrame.
# Calculate the average grade for each student.
# Filter and display students with an average grade above 75.

# Importing the required library
import pandas as pd

# Load the CSV file into a DataFrame
file_path = "student_grades.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Calculate the average grade for each student, ignoring non-numeric columns
data['Average_Grade'] = data.iloc[:, 1:].mean(axis=1)

# Display the DataFrame with average grades
print("All students with their average grades:")
print(data)

# Filter students with an average grade above 75
high_achievers = data[data['Average_Grade'] > 75]

# Display students with an average grade above 75
print("\nStudents with an average grade above 75:")
print(high_achievers)
