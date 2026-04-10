import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# === CHART 1: Profit by Category ===
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_profit.index, category_profit.values, color=["blue", "green", "red"])
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()
print("Chart 1 saved!")

# === CHART 2: Sales by Region ===
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values, color="orange")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
print("Chart 2 saved!")