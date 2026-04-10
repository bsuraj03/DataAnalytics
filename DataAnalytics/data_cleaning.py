import pandas as pd

#Data
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# === STEP 1: Check for missing values ===
print("=== Missing Values ===")
print(df.isnull().sum())

# === STEP 2: Check for duplicates ===
print("\n=== Duplicate Rows ===")
print("Total duplicates:", df.duplicated().sum())

# === STEP 3: Check data types ===
print("\n=== Data Types ===")
print(df.dtypes)

# === STEP 4: Check shape ===
print("\n=== Shape ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# === STEP 5: Fix date columns ===
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\n=== Fixed Data Types ===")
print(df["Order Date"].dtype)
print(df["Ship Date"].dtype)

# === STEP 6: Extract useful info from dates ===
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("\n=== New Columns Added ===")
print(df[["Order Date", "Ship Date", "Order Year", "Order Month", "Shipping Days"]].head())

# === STEP 7: Analyze Shipping Days by Ship Mode ===
print("\n=== Average Shipping Days by Ship Mode ===")
print(df.groupby("Ship Mode")["Shipping Days"].mean().sort_values())

# === STEP 8: Any suspiciously long shipping times? ===
print("\n=== Orders that took more than 7 days ===")
late_orders = df[df["Shipping Days"] > 7]
print("Total late orders:", len(late_orders))
print(late_orders[["Order ID", "Ship Mode", "Shipping Days"]].head())