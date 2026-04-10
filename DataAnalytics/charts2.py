import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

#CHART 1 : Line Chart - Sales over Time
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
yearly_sales = df.groupby("Year")["Sales"].sum()

plt.figure(figsize=(8, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker="o", color="blue")
plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("yearly_sales.png")
plt.show()
print("Chart 1 done!")

# === CHART 2: Pie Chart - Sales by Region ===
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.savefig("sales_by_region_pie.png")
plt.show()
print("Chart 2 done!")

# === CHART 3: Seaborn - Profit by Category ===
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Profit", estimator=sum)
plt.title("Profit by Category (Seaborn)")
plt.tight_layout()
plt.savefig("profit_seaborn.png")
plt.show()
print("Chart 3 done!")
