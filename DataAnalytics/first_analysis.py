import pandas as pd
import numpy as ny

#create your first dataset
data = {
    "Name" : ["Ted", "Barney", "Lily", "Marshall", "Robin"],
    "Age" : [33, 32, 31, 34, 30],
    "Salary" : [20000, 100000, 15000, 90000, 25000]
}

#convert to a dataframe
df = pd.DataFrame(data)

#Let's Explore It
print("=== First 5 Rows ===")
print(df.head())

print("\n=== Basic Statistics ===\n")
print(df.describe())

print("\n=== Average Salary ===\n")
print(df["Salary"].mean())

print("\n=== Highest Paid Person ===")
print(df[df["Salary"] == df["Salary"].max()])

