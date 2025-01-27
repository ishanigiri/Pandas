import pandas as pd
data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "eve"],
    "Salary": [50000, 70000, 45000, 8000, 6000]
}
df = pd.DataFrame(data)
#Group by department and calculate average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("Average salary by department:")
print(avg_salary)