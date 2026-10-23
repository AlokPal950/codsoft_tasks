
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("data.csv")

# Set a consistent chart style
sns.set_theme(style="whitegrid")

# 2. Bar Chart: Average salary by department
department_salary = df.groupby("Department")["Salary"].mean()

department_salary.plot(
    kind="bar",
    title="Average Salary by Department",
    color="steelblue",
    edgecolor="black"
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# 3. Line Chart: Salary by employee ID
plt.figure(figsize=(8, 5))

plt.plot(
    df["EmployeeID"],
    df["Salary"],
    marker="o",
    color="green",
    label="Employee Salary"
)

plt.title("Salary by Employee ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# 4. Pie Chart: Employees by department
department_count = df["Department"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Employee Distribution by Department")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# 5. Histogram: Salary distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["Salary"],
    bins=6,
    color="orange",
    edgecolor="black"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# 6. Scatter Plot: Experience vs Salary
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department",
    s=100
)

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

print("All charts created successfully!")
