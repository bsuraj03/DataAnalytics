import pandas as pd

#LOAD THE REAL DATASET
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

#First look at the data
print("=== Shape (Rows, Columns) ===")
print(df.shape)

print("\n=== Column Names ===")
print(df.columns.tolist())

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Basic Statistics ===")
print(df.describe())

# === BUSINESS INSIGHTS ===

# 1. Total Sales and Profit
print("=== Total Sales & Profit ===")
print("Total Sales: $", round(df["Sales"].sum(), 2))
print("Total Profit: $", round(df["Profit"].sum(), 2))

# 2. Most profitable category
print("\n=== Profit by Category ===")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# 3. Which region makes the most sales?
print("\n=== Sales by Region ===")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# 4. Top 5 most profitable products
print("\n=== Top 5 Profitable Products ===")
print(df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head())