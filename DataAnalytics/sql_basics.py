import pandas as pd
import sqlite3

# Load CSV into a SQLite database
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Create a database connection
conn = sqlite3.connect("superstore.db")

# Save dataframe as a SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Database created successfully!")

# === QUERY 1: Basic SELECT ===
query1 = "SELECT * FROM orders LIMIT 5"
result1 = pd.read_sql(query1, conn)
print("\n=== First 5 rows ===")
print(result1[["Customer Name", "Category", "Sales", "Profit"]])

# === QUERY 2: Total Sales ===
query2 = "SELECT SUM(Sales) as Total_Sales FROM orders"
result2 = pd.read_sql(query2, conn)
print("\n=== Total Sales ===")
print(result2)

# === QUERY 3: Sales by Region ===
query3 = """
SELECT Region, SUM(Sales) as Total_Sales 
FROM orders 
GROUP BY Region 
ORDER BY Total_Sales DESC
"""
result3 = pd.read_sql(query3, conn)
print("\n=== Sales by Region ===")
print(result3)

#conn.close()

conn = sqlite3.connect("superstore.db")

# === QUERY 4: WHERE clause (filtering) ===
query4 = """
SELECT [Customer Name], Sales, Profit 
FROM orders 
WHERE Profit < 0 
LIMIT 10
"""
result4 = pd.read_sql(query4, conn)
print("\n=== Loss Making Orders ===")
print(result4)

# === QUERY 5: COUNT ===
query5 = """
SELECT Category, COUNT(*) as Total_Orders
FROM orders
GROUP BY Category
ORDER BY Total_Orders DESC
"""
result5 = pd.read_sql(query5, conn)
print("\n=== Orders by Category ===")
print(result5)

# === QUERY 6: Average discount by region ===
query6 = """
SELECT Region, ROUND(AVG(Discount) * 100, 2) as Avg_Discount_Percent
FROM orders
GROUP BY Region
ORDER BY Avg_Discount_Percent DESC
"""
result6 = pd.read_sql(query6, conn)
print("\n=== Average Discount by Region ===")
print(result6)

conn.close()
