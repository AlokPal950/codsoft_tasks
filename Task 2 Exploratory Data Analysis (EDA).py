
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

# 2. Examine the dataset structure
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

# 3. Generate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Analyze salary distribution
print("\nSalary Statistics:")
print("Average Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())

# 6. Analyze department-wise salary
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# 7. Count employees in each department
print("\nEmployees by Department:")
print(df["Department"].value_counts())

# 8. Find relationships between numeric variables
print("\nCorrelation Matrix:")
print(
    df[["Age", "Salary", "Experience", "PerformanceScore"]]
    .corr()
)

# 9. Detect salary outliers using the IQR method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print("\nSalary Outliers:")
print(outliers[["Name", "Department", "Salary"]])

# 10. Create a salary distribution chart
plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=6, edgecolor="black")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()

# 11. Create a department-wise salary chart
department_salary = df.groupby("Department")["Salary"].mean()

department_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("department_salary.png")
plt.show()

# 12. Answer business questions
print("\nBusiness Findings:")
print("Total Employees:", len(df))
print("Highest Paid Employee:", df.loc[df["Salary"].idxmax(), "Name"])
print("Highest Salary:", df["Salary"].max())
print("Average Employee Salary:", round(df["Salary"].mean(), 2))

print("\nEDA completed successfully.")
