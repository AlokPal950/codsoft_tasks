
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("data.csv")

print("Original Dataset:")
print(df)

# 2. Inspect the dataset structure
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

# 3. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Check for duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 5. Correct inconsistent text entries
df["Name"] = df["Name"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# 6. Correct data types
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["JoiningDate"] = pd.to_datetime(
    df["JoiningDate"], errors="coerce"
)

# 7. Remove duplicate records
df = df.drop_duplicates()

# 8. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Name"] = df["Name"].fillna("Unknown")

# 9. Check the cleaned data types
print("\nCleaned Data Types:")
print(df.dtypes)

# 10. Save the cleaned dataset
df.to_csv("data_cleaned.csv", index=False)

print("\nCleaned Dataset:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

print("\nCleaned dataset saved as data_cleaned.csv")
